---
layout: post
title: "使用CSS3改变文本选中的颜色"
category: Past
description: 今天发现TechCrunch中文网站文字选区是绿色，跟网站整体风格非常协调。
---
今天打开TechCrunch的中文网站，选中文字时选区颜色变成了绿色，跟网站整体的绿色风&#26684;非常协调。于是对实现细节感兴趣，一探究竟。

实现很简单，利用CSS3的特性。

``` css
::selection{
  background-color:#84ca7f;color:#000;
}
::-webkit-selection{
  background-color:#84ca7f;color:#000;
}
::-moz-selection{
  background-color:#84ca7f;color:#000;
}
```

同样可以使用CSS选择器指定部分元素设置选区颜色，例如.maroon::selection。IE系列，我只有IE9，也支持该特性。

我觉得修改选区默认颜色要谨慎，除非能够像TechCrunch那样达到整体风格统一。否则可能令用户不习惯。