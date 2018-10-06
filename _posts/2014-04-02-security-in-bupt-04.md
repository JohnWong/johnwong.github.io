---
layout: post
title: "扒一扒北邮的安全问题[4]-一大波访问控制问题"
category: past
description: 毕业前把自己无聊玩的抖出来。
thumb: /images/2014-04-02-security-in-bupt-04-03.png
---

#### 漏洞类型： 

弱口令/无访问控制/代码备份

#### 相关网站

内网多个ip

#### 问题描述

文件、数据库、代码、phpMyAdmin等无法访问控制或者弱口令

#### 漏洞详情

一票Web容器没做访问控制，同时给了列目录权限。这样就等于自己的各种资源分享给了所有人啊，这应该不是初衷吧。 

![/images/2014-04-02-security-in-bupt-04-01.png](/images/2014-04-02-security-in-bupt-04-01.png)

然后还有一票phpMyAdmin没有访问控制，或者弱口令。据说拿到MySql的远程登录权限甚至能上传程序控制整个主机。 

![/images/2014-04-02-security-in-bupt-04-02.jpg](/images/2014-04-02-security-in-bupt-04-02.jpg)

然后是使用默认密码的版本控制程序、惠普打印机、戴尔服务器、中兴4G LTE CPE设备、TP-LINK路由器。这个打印机还有Telnet功能，能远程打印。至于有没有打印出来不知道了。 


![/images/2014-04-02-security-in-bupt-04-03.png](/images/2014-04-02-security-in-bupt-04-03.png)

![/images/2014-04-02-security-in-bupt-04-04.png](/images/2014-04-02-security-in-bupt-04-04.png)

![/images/2014-04-02-security-in-bupt-04-05.png](/images/2014-04-02-security-in-bupt-04-05.png)

![/images/2014-04-02-security-in-bupt-04-06.png](/images/2014-04-02-security-in-bupt-04-06.png)

![/images/2014-04-02-security-in-bupt-04-07.png](/images/2014-04-02-security-in-bupt-04-07.png)
 
最后是一个智慧油田系统。数据库没有使用弱口令，但是把源代码打包放到Web容器里，很容易从中找到数据库配置。管理员密码还是明文存储的。。。 

![/images/2014-04-02-security-in-bupt-04-08.png](/images/2014-04-02-security-in-bupt-04-08.png)

总结一下：使用web容器最好不要给列目录的权限；不使用弱口令和默认密码；代码不要打包后放到容器中。 
PS. 我尽量隐藏IP等细节了。如果不小心放出了请即使私信我。 

#### 原帖

[http://bbs.byr.cn/#!article/WWWTechnology/24398](http://bbs.byr.cn/#!article/WWWTechnology/24398)