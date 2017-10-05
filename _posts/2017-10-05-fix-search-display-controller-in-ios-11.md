---
layout: post
title: "修复iOS 11上UISearchDisplayController的问题"
category: mobile
description: 修复iOS 11上UISearchDisplayController的问题
thumb: /images/2017-10-05-fix-search-display-controller-in-ios-11.jpg
---

中秋假期比较空闲，把许久没维护的今日公交是配到iPhone X，修复了两个小问题。适配过程中遇到UISearchDisplayController的问题，尝试解决了下。虽然UISearchDisplayController已经废弃建议更换为UISearchController，但是更换逻辑改动比较大，没有尝试。

出现的问题表现在，设置了search bar高度固定，竖屏点击search bar，蒙层位置错误。点击search bar后唤起搜索界面，在切换到横屏界面错乱。解决方法是在`-[UIViewController viewDidLayoutSubviews]`方法里调整布局。

```objc
- (void)adjustSearchBar
{
    dispatch_async(dispatch_get_main_queue(), ^{
        UISearchBar *searchBar = self.searchController.searchBar;
        searchBar.height = self.searchBarHeight.constant;
        UITextField *textField = [searchBar safeValueForKey:@"_searchField"];
        if (textField) {
            textField.centerY = searchBar.height / 2;
        }

        UIButton *cancelButton = [searchBar safeValueForKey:@"_cancelButton"];
        if (cancelButton) {
            cancelButton.centerY = searchBar.height / 2;
        }

        UIView *containerView = [self.searchController safeValueForKey:@"_containerView"];
        if ([containerView isKindOfClass:NSClassFromString(@"UISearchDisplayControllerContainerView")]) {
            UIView *topView = [containerView safeValueForKey:@"_topView"];
            UIView *bottomView = [containerView safeValueForKey:@"_bottomView"];
            topView.top = searchBar.top;
            topView.height = searchBar.height;
            bottomView.top = topView.bottom;
            bottomView.height = containerView.height - bottomView.top;
        }
    });
}
```

这里一些私有变量的获取没有使用`valueForKey`方法，因为这样可能提前触发getter方法导致界面展示有问题。因此给`NSObject`增加了一个方法，如果存在ivar则直接访问ivar不触发getter。方法如下：

```objc
@implementation NSObject (ValueForKey)

- (nullable id)safeValueForKey:(NSString *)key
{
    if (key.length == 0) {
        return nil;
    }
    Ivar ivar = class_getInstanceVariable(self.class, key.UTF8String);
    if (ivar) {
        return object_getIvar(self, ivar);
    }
    if (class_getInstanceMethod(self.classForCoder, NSSelectorFromString(key))) {
        return [self valueForKey:key];
    }
    return nil;
}

@end
```