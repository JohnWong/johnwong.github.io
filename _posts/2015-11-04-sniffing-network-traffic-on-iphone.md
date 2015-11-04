---
layout: post
title: iPhone网络请求捕获
category: mobile
description: 掌握iPhone网络抓包大法
thumb: /images/2015-11-04-sniffing-network-traffic-on-iphone.png
---

最近工作中刚好遇到需要iPhone上调试网络请求的问题。虽没什么技术含量，但是可以写下来当作笔记。

## Charles

业界俗称花瓶，网络请求抓包非常好用。最新版本3.11.1，已经解决了之前几个版本的一些问题，比如界面模糊、command+n不能新建session、https无法解析。使用起来非常顺手。用法：

1. Charles->Proxy->Proxies，设置http端口号。
2. 设备网络设置代理，ip写mac的ip，端口号写上面的。

如果网络请求是https的，记得到`Charles->Proxy->SSL Proxy Settings`添加要捕获的域名。除了一般的网路请求捕获外，还可以mock请求等等。唯一的缺点就是————价格有点贵。

## Wireshark

Wireshark是一款很强大的免费的网络抓包工具。以前只知道Wireshark可以捕获本地流量，今天了解了如何捕获iOS设备流量。


1. rvictl -s UDID - (id of device 20 chars, you can locate 4t in iTunes or organiser in Xcode)
2. sudo launchctl list com.apple.rpmuxd
3. sudo tcpdump -n -t -i rvi0 -q tcp OR just sudo tcpdump -i rvi0 -n 
4. Wireshar选择网卡rvi0，开始捕获

参考：[Stack Overflow](http://stackoverflow.com/questions/1598407/iphone-and-wireshark)



