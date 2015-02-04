---
layout: post
title: iOS8定位适配
category: Mobile
description: iOS8推出后定位做了改动，不适配无位可定。
thumb: "/images/2014-09-22-core-location-in-ios8.png"
---
iOS8 beta版发布后淘点点尝试适配，其中遇到的一个主要的问题是无法定位，做了一些适配后后能够正常定位。iOS8正式版定位方面没有变动，依然需要做适配。iOS8对定位的改动，基本思路就是将定位细分为Always和WhenInUse两类，要求开发者说明使用定位的用途并酌情使用。此举意在防止定位信息滥用，至于作用就仁者见仁智者见智了。

> 更新：  
> 当使用iOS SDK 8，并且iOS设备或模拟器也是iOS8时，无法定位需要做适配。其他情况下不做适配也可以正常工作。

## 定位变更

iOS8的变更包括：

- 状态栏图标
- 定位服务设置
- 定位授权

想要全面了解的同学可以学习WWDC的`What's New in Core Location`一节。这里我们主要介绍定位授权。

定位授权在iOS8中细分为Always和WhenInUse。如下表，定位可以细分为5类。前三个前台更新，属于Continuous Updates。后两个后台更新，属于Location Monitoring。Always授权可以使用这5类定位，而WhenInUse可以使用Continuous Updates，也就是前三个。

| Location                     | Always| WhenInUse|
| ---------------------------- |:-----:| --------:|
| Location                     | Yes   | Yes      |
| Background location          | Yes   | Yes      |
| Ranging                      | Yes   | Yes      |
| Region monitoring            | Yes   |          |
| Significant location changes | Yes   |          |

iOS8要求应用如果使用定位，需要告诉用户使用的原因。描述放在应用的Info.plist中，当然也可能是其他文件名，取决于项目中的定义。两个授权的key分别为：

 - NSLocationAlwaysUsageDescription
 - NSLocationWhenInUseUsageDescription
 
看起来Always授权涵盖了WhenInUse授权，使用Always授权可以一劳永逸了。但是如果应用被授予了Always授权，几天后可能需要再次向用户请求授权。这样是为了让应用按需申请授权，开发者可能需要权衡。

之前定位授权获取发生在应用使用定位的时候，开发者不需要显式地请求。现在则需要显式地请求授权。两个授权对应的方法在类`CLLocationManager`中，分别为：

``` objective-c
- (void)requestAlwaysAuthorization __OSX_AVAILABLE_STARTING(__MAC_NA, __IPHONE_8_0);
- (void)requestWhenInUseAuthorization __OSX_AVAILABLE_STARTING(__MAC_NA, __IPHONE_8_0);
```

## 如何适配

### 1. 添加定位使用描述

在Info.plist中添加应用准备使用的定位授权，例如

``` xml
<key>NSLocationAlwaysUsageDescription</key>
<string>淘点点将获取您的位置，为您提供更精准的餐饮服务</string>
```

### 2. 检测并请求授权
在调用`CLLocationManager`的`startUpdatingLocation`前请求授权。首先为了兼容老版本，需要用宏定义在老版本中屏蔽相关代码。然后检测Info.plist中定义授权的描述，根据存的授权的描述决定申请哪个定位授权。以下代码为墨昕编写。


``` objective-c
#if __IPHONE_OS_VERSION_MAX_ALLOWED > __IPHONE_7_1
    if (floor(NSFoundationVersionNumber) > NSFoundationVersionNumber_iOS_7_1 && [CLLocationManager authorizationStatus] == kCLAuthorizationStatusNotDetermined) {
        BOOL hasAlwaysKey = [[NSBundle mainBundle] objectForInfoDictionaryKey:@"NSLocationAlwaysUsageDescription"] != nil;
        BOOL hasWhenInUseKey = [[NSBundle mainBundle] objectForInfoDictionaryKey:@"NSLocationWhenInUseUsageDescription"] != nil;
        if (hasAlwaysKey) {
            [self.locationManager requestAlwaysAuthorization];
        } else if (hasWhenInUseKey) {
            [self.locationManager requestWhenInUseAuthorization];
        } else {
            NSAssert(hasAlwaysKey || hasWhenInUseKey, @"moxin.xt:add NSLocationWhenInUseUsageDescription or NSLocationAlwaysUsageDescription to your info.plist");
        }
    }
#endif
```

同时建议其他iOS团队写好对用户授权的描述，更多信息参考[在正确的情境中向用户获取iOS权限](http://www.cocoachina.com/design/20140414/8151.html)

## Refer

[WWDC 2014](https://developer.apple.com/videos/wwdc/2014/) What's New in Core Location一节

[Stack Overflow](http://stackoverflow.com/questions/24062509/ios-8-location-services-not-working)

[CoreLocation Framework Reference](https://developer.apple.com/library/ios/documentation/CoreLocation/Reference/CLLocationManager_Class/index.html)