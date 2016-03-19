---
layout: post
title: "笔记本连接Cisco: LEAP网络"
category: past
description: "公司无线覆盖，但是加密类型是Cisco: LEAP遇到一点问题。"
---
笔记本是Thinkpad T420i。公司无线覆盖，但是加密类型是Cisco: LEAP。直接连接，在无线网络的加密类型中找不到这个。病急乱投医，插上Realtec 8188 USB网卡，安装USB网卡的驱动，然后就能连接无线了。拔掉USB网卡，使用自带网卡，依然能够连接。卸载了USB网卡驱动，又无法连接了。

顺带说一句，笔记本的网卡是Realtec的。同样是一家厂出的，USB网卡支持LEAP，自带网卡不支持。装了USB网卡的驱动，自带网卡也支持。这是神一样的逻辑，真不知道厂家是怎么想的。

手机连接Cisco LEAP网络参考[http://www.dotblogs.com.tw/bowwowxx/archive/2010/07/22/16686.aspx](http://www.dotblogs.com.tw/bowwowxx/archive/2010/07/22/16686.aspx)

