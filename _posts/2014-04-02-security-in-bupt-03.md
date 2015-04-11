---
layout: post
title: "扒一扒北邮的安全问题[3]-摄像头这么多"
category: Security
description: 毕业前把自己无聊玩的抖出来。
thumb: /images/2014-04-02-security-in-bupt-03-01.png
---

#### 漏洞类型： 

弱口令/默认密码

#### 相关网站

校园内网某实验室

#### 问题描述

海康威视Web登录界面使用默认密码 

#### 漏洞详情

之前发现的问题，扫到某个ip，发现开放80端口。打开发现是摄像头的Web登录界面，好高端啊。 
Google得到这个产品的默认密码，居然可以登录。后来发现乌云上也有人报过这个漏洞，由于主要原因是用户没有修改登录密码，因此被厂商忽略了。12个网络摄像头，好高端啊。至于哪个实验室的不太清楚。该实验室还有另外一个摄像头，这里就懒得截图了。

![2014-04-02-security-in-bupt-03-01.png](//dn-johnwong.qbox.me/images/2014-04-02-security-in-bupt-03-01.png)

PS. 类似默认密码的海康威视的设备可以通过神器[钟馗之眼](http://www.zoomeye.org/)找到更多。

#### 原帖

[http://bbs.byr.cn/#!article/WWWTechnology/24327](http://bbs.byr.cn/#!article/WWWTechnology/24327)