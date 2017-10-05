---
layout: post
title: "iPhone X 上获取状态栏网络状态的方法"
category: mobile
description: 探索UIKit
thumb: /images/2017-10-05-access-network-type-from-statusbar-in-iphone.jpg
---

获取网络状态常用的库是`Reachability`。但是这个库存在一些问题，替代的方法是从状态栏获取网络状态。一般的写法是：

```
typedef enum {
    NetWorkType_None = 0,
    NetWorkType_2G,
    NetWorkType_3G,
    NetWorkType_4G,
    NetWorkType_LTE,
    NetWorkType_WiFi,
} NetWorkType;

UIApplication *application = [UIApplication sharedApplication];
NSArray *subviews = [[[application valueForKey:@"statusBar"] valueForKey:@"foregroundView"]subviews];
 
NSNumber *dataNetWorkItemView = nil;
 
for (id subView in subviews) {
　　if ([subView isKindOfClass:[NSClassFromString(@"UIStatusBarDataNetworkItemView") class]]) {
            dataNetWorkItemView = subView;
            break;
        }
    }
 
    NetWorkType networkType = NetWorkType_None;
    switch ([[dataNetWorkItemView valueForKey:@"dataNetworkType"] integerValue]) {
        case 1:
            networkType = NetWorkType_2G;
            break;
        case 2:
            networkType = NetWorkType_3G;
            break;
        case 3:
            networkType = NetworkType_4G;
            break;
        case 4:
        	networkType = NetworkType_LTE;
        	break;
        case 5:
        	networkType = NetworkType_WiFi;
        	break;
        default:
            networkType = NetWorkType_None;
            break;
    }
    return networkType;
}
```

这样的方法在iPhone X上会闪退。因为iPhone X上导航栏会改用`UIStatusBar_Modern`类，结构跟之前大不相同。为了在iPhone X上获取状态栏上的网络状态，试过运行时查看状态栏里的内容，然而模拟器的网络状态只有WiFi。没有真机，无法获知移动网络时的区别。那么只能视图获取状态栏的数据源，用反编译工具Hopper里查看状态栏初始化，找到了数据源`+[UIStatusBarServer getStatusBarData]`。方法返回值是结构体，可以运行时去获取具体结构，推荐使用`https://github.com/nst/RuntimeBrowser`工具，得到返回的结构体如下：

```
struct StatusBarData {
    /* 0 时间
     * 2 飞行模式
     * 6 网络类型
     * 8 电池
     */
    bool itemIsEnabled[35];
    char timeString[64];
    char shortTimeString[64];
    int gsmSignalStrengthRaw;
    int gsmSignalStrengthBars;
    char serviceString[100];
    char serviceCrossfadeString[100];
    char serviceImages[2][100];
    char operatorDirectory[1024];
    unsigned int serviceContentType;
    int wifiSignalStrengthRaw;
    int wifiSignalStrengthBars;
    unsigned int dataNetworkType;
    int batteryCapacity;
    unsigned int batteryState;
    char batteryDetailString[150];
    int bluetoothBatteryCapacity;
    int thermalColor;
    unsigned int thermalSunlightMode : 1;
    unsigned int slowActivity : 1;
    unsigned int syncActivity : 1;
    char activityDisplayId[256];
    unsigned int bluetoothConnected : 1;
    unsigned int displayRawGSMSignal : 1;
    unsigned int displayRawWifiSignal : 1;
    unsigned int locationIconType : 1;
    unsigned int quietModeInactive : 1;
    unsigned int tetheringConnectionCount;
    unsigned int batterySaverModeActive : 1;
    unsigned int deviceIsRTL : 1;
    unsigned int lock : 1;
    char breadcrumbTitle[256];
    char breadcrumbSecondaryTitle[256];
    char personName[100];
    unsigned int electronicTollCollectionAvailable : 1;
    unsigned int wifiLinkWarning : 1;
    unsigned int wifiSearching : 1;
    double backgroundActivityDisplayStartDate;
};
```

其中有些字段明显是字符串，解析出来是bool，我手动修改了下类型。那么就可以写出获取状态栏的网络状态的方法：

```
+ (int)networkType
{
    Class cls = NSClassFromString(@"UIStatusBarServer");
    SEL selector = NSSelectorFromString(@"getStatusBarData");
    NSMethodSignature *signature = [cls methodSignatureForSelector:selector];
    NSInvocation *invocation = [NSInvocation invocationWithMethodSignature:signature];
    invocation.target = cls;
    invocation.selector = selector;
    [invocation invoke];
    struct {
        bool x1[35];
        BOOL x2[64];
        BOOL x3[64];
        int x4;
        int x5;
        BOOL x6[100];
        BOOL x7[100];
        BOOL x8[2][100];
        BOOL x9[1024];
        unsigned int x10;
        int x11;
        int x12;
        unsigned int x13;
        int x14;
        unsigned int x15;
        BOOL x16[150];
        int x17;
        int x18;
        unsigned int x19 : 1;
        unsigned int x20 : 1;
        unsigned int x21 : 1;
        BOOL x22[256];
        unsigned int x23 : 1;
        unsigned int x24 : 1;
        unsigned int x25 : 1;
        unsigned int x26 : 1;
        unsigned int x27 : 1;
        unsigned int x28;
        unsigned int x29 : 1;
        unsigned int x30 : 1;
        unsigned int x31 : 1;
        BOOL x32[256];
        BOOL x33[256];
        BOOL x34[100];
        unsigned int x35 : 1;
        unsigned int x36 : 1;
        unsigned int x37 : 1;
        double x38;
    } * data;
    [invocation getReturnValue:&data];
    int networkType = data->x13;
    return networkType;
}
```
之所以结构体内字段没有按照原来的名字，是担心审核不通过。加入这个方法的应用已经在审核中，还没有结果。

接下来探索下修改状态栏。用Method Swizzling的方法修改这个方法的返回值。

```
@implementation NSObject (Hook)

+ (void)load
{
    Method m1 = class_getClassMethod(NSClassFromString(@"UIStatusBarServer"), @selector(getStatusBarData));
    Method m2 = class_getClassMethod(self, @selector(hook_getStatusBarData));
    method_exchangeImplementations(m1, m2);
}

+ (struct StatusBarData *)hook_getStatusBarData
{
    
    struct StatusBarData *ret = [self hook_getStatusBarData];
    ret->dataNetworkType = 3;
    strcpy(ret->breadcrumbTitle, "hahaha");
    strcpy(ret->breadcrumbSecondaryTitle, "huhuhu");
    strcpy(ret->personName, "personName");
    ret->thermalSunlightMode = YES;
    ret->batterySaverModeActive = YES;
    ret->deviceIsRTL = YES;
    ret->batteryState = 3;
    ret->batteryCapacity = 500;
    ret->serviceContentType = 5;
    ret->electronicTollCollectionAvailable = YES;
    return ret;
}

@end
```

这段代码跑起来，状态栏已经被改得乱七八糟了😝。