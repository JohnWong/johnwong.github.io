---
layout: post
title: "PhoneGap开发的一点体会"
category: past
description: 在一个被坑了的外包项目中使用PhoneGap的一点体会。
---
1. viewport可以在加载的时候通过js来动态设置，如果想通过viewport来缩放以解决分辨率适配的问题，必须将user-scalable设为yes。这样导致的问题是页面中的float设为fixed的元素不会固定。同样要使fixed生效必须使用user-scalable=no。设为可缩放的时候jquery等等的固定的ui均失效。真是个鱼与熊掌不可得兼的问题。最后的解决办法是将body的css加入zoom属性，通过zoom来控制页面缩放。body的背景图片缩放使用background-size:640px
 auto;可以实现。这样这个问题完美解决了

2. 底部固定的元素本可以覆盖到屏幕边框，但是底部有时粗线滚动条导致出现缝隙，办法是bottom属性设为负几。

3. phonegap的音乐播放功能真是相当不稳定。同一首歌曲有时候点播放就播放了，有时候播放没反应。官方说media的API不完全符合html5，以后可能会修改。目前最现实的办法是播放的时候，在检测播放进度的timer里面检测到用户点击过播放但是当前position为负，就再次调用play方法。还有悲剧的是页面返回后仍然在播放，需要在页面返回前调用media停止的方法

4. phonegap不支持视频文件播放。可能通过webintent解决，我实验失败了

不得不说通过css来控制缩放，实现适配分辨率，真是解决了Android原生布局一大问题啊！

