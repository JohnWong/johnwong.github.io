---
layout: post
title: iOS开发的奇技淫巧
category: Mobile
description: 说多了都是泪
thumb: images/2015-07-04-ios-quirks1.png
---

## UIRefreshControl的使用

UIRefreshControl的使用方法一般是在UIControlEventValueChanged事件时触发，也就是下拉到一定程度的时候触发。这样可能出现的问题是下拉释放后很快调用`-endRefresh`，动画不流畅。可以在`－scrollViewDidEndDragging:willDecelerate:`时判断下拉程度来触发，或者延迟调用`-endRefresh`。最后找到了看起来完美的方法，在下拉释放回弹后调用。也就是在`-scrollViewDidEndDecelerating:`中调用，代码如下：

``` objective-c
- (void)scrollViewDidEndDecelerating:(UIScrollView*)scrollView
{    
    if( self.refreshControl.isRefreshing )
        [self refresh];
}
```

See [StackOverflow](http://stackoverflow.com/a/15591984/3284570)

## UIRefreshControl下拉动画的位置控制

默认下拉时，UIRefreshControl的位置会固定在scrollview的上方，在下拉时会露出来。

![iOS Quirks 1](/images/2015-07-04-ios-quirks-1.gif)

给UIRefreshControl加入背景色，即使是clearColor，它的位置将会随着下拉逐渐从上部出现。

![iOS Quirks 2](/images/2015-07-04-ios-quirks-2.gif)

## UITableView的header阻止浮动

UITableView使用UITableViewStylePlain样式时，section的header与footer会在滚动过程中固定在顶部，这个交互很不错。如果要阻止这个交互，那么办法有四个：1. 样式改成UITableViewStyleGrouped，但是在iOS6上需要做很多样式调整才能达到与UITableViewStylePlain一致；2. 每个section多加行来模拟header或footer，但是代码维护难度更大；3. 继承UITableView，覆盖方法`-allowsHeaderViewsToFloat`或`-allowsFooterViewsToFloat`，但是使用了私有API审核有风险；4. 自定义header或者footer阻止浮动。我认为第四种方法最优。在`-setFrame:`的时候将frame设置为我们希望的位置。代码如下：

```objective-c
- (instancetype)initWithTableView:(UITableView *)tableView section:(NSInteger)section type:(O2OTableViewSectionType)type {
    self = [super init];
    if (self) {
        self.tableView = tableView;
        self.section = section;
        self.type = type;
    }
    return self;
}

- (void)setFrame:(CGRect)frame{
    CGRect sectionRect = [self.tableView rectForSection:self.section];
    CGFloat top = 0;
    switch (self.type) {
        case O2OTableViewSectionHeader:
            top = CGRectGetMinY(sectionRect);
            break;
        case O2OTableViewSectionFooter:
            top = CGRectGetMaxY(sectionRect) - CGRectGetHeight(frame);
        default:
            break;
    }
    CGRect newFrame = CGRectMake(CGRectGetMinX(frame),
                                 top,
                                 CGRectGetWidth(frame),
                                 CGRectGetHeight(frame));
    [super setFrame:newFrame];
}

```

## iOS7地图标记的offset设置无效

在地图上设置自定义标记的时候，经常需要修改图片的偏移来标记到正确的位置。在iOS7上设置centerOffset无效。这是iOS7上的一个bug，修复的办法如下：

``` objective-c
@implementation TBCityAnnotationView

@synthesize centerOffset = _centerOffset;

- (void)setCenterOffset:(CGPoint)centerOffset {
    _centerOffset = centerOffset;
}

@end
```

See [StackOverflow](http://stackoverflow.com/a/19794084/3284570)

## 修改UITableView为空时样式

在StoryBoard上拖出来UITableView时，UITableView为空的时候的样式是上面下拉刷新的图那样，放置了一些占位的行。要想阻止这个默认行为，展示空白，只需要设置footerView：

``` objective-c
tableView.tableFooterView = [[UIView alloc] init];
```



