---
layout: post
title: "Nvidia Shield 刷机踩坑"
category: mobile
description: 最强电视盒子
thumb: /images/2019-03-28-nvidia-shiled-recovery-image-flash.jpg
---

买了电视盒子神器 nvidia shiled，用起来感觉性能确实不错，配上索尼电视看4K很爽。使用了一段时间想看看Youtube和Twitch，路由器翻墙，装了谷歌服务，也能看。谷歌的商店安装应用偶尔会有一些问题，也凑合能用。最棘手的是盒子自带了奇异玩应用商店，爱奇艺和优酷之类的应用更新必须通过这个商店。商店里的版本很老不更新，感觉几乎是放弃的状态。用adb调试也可以安装，但是每次要用电脑还是麻烦。还有语音识别，经常识别错误。于是就萌生了安装美版的想法，体验下原装的shiled。

主要参考的文档包括：
- [Nvidia Shield TV 2017 国行刷美版固件指南
](https://github.com/JACK-THINK/Nvidia-Shield-TV-2017-Cookbook/blob/master/How%20to%20flash%20Nvidia%20Shield%20TV%202017%20China%20Editon%20with%20the%20Android%20generic%20recovery%20image.md)
- [HowTO Flash Recovery Image](http://developer.download.nvidia.com/mobile/shield/ROM/SHIELD_ATV/6.3.0/HowTo-Flash-Recovery-Image.txt)
- [Nvidia Shield 下载中心](https://developer.nvidia.com/gameworksdownload#?tx=$additional,shield)

下载中心固件这里有区分平台 Windows 和 Linux。我用的是 Mac，本以为跟 Linux很接近，用到的 adb 和 fastboot 也都已经安装，就直接用 Mac 去刷机。结果刷机过程中会卡在刷镜像不动，试过好多个镜像都不成功。心里一凉，感觉要变砖了。后面试试装了 Windows 虚拟机来刷，竟然没有遇到问题，很顺利刷机成功了。万万没想到对 Mac 的兼容性比 Windows 要差。还好救回来了。

原生系统装 Youtube、Netflix 和 Twitch 很顺利。安装优酷爱奇艺也没遇到障碍。唯一不太好用的地方是国内好多应用都没有针对Android TV开发，不会在桌面上露出应用图标。之前的桌面有其他应用的入口可以点进来，新版的桌面没有这个入口了。后面安装了HALauncher，进这种应用会方便一些。
