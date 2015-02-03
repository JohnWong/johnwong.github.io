---
layout: post
title: "苹果的一些坑"
category: Past
description: 汇总近期遇到的苹果的Bug。
thumb: /images/2014-06-04-bugs-by-apple.jpg
---
嗯嗯，最近踩坑不少，总结一下：

1. OSX中文系统网络代理，如果设置了排除的网址，保存后会被系统将分隔符逗号改为顿号导致失效。所以我一直在用英文版。

2. iOS地图SDK中，MKAnnotationView的centerOffset属性设置无效，是一个bug。

3. iOS8槽点更多。模拟器点击关于本机之后有可能卡死。5s进入设置页点进比较深的页面，然后快速双击后退。页面内容后退两次，但是导航栏只后退了一次。AppStore闪退过。AppStore点击搜索后自动变成取消搜索的状态。wifi设置bug很多，经常变成怪异的样子。

4. Safari中有的图片会缺少一部分，试过Photoshop导出图片的各种选项后发现，导出时勾选连续、使用嵌入颜色配置才会显示正确。

