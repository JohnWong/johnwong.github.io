---
layout: post
title: "扒一扒北邮的安全问题[2]-如何查看女神照片"
category: Security
description: 毕业前把自己无聊玩的抖出来。
thumb: /images/2014-04-01-security-in-bupt-02-02.png
---

#### 漏洞类型： 

SQL注入

#### 相关网站

研究生信息数字化管理系统 

#### 问题描述

SQL注入漏洞导致部分学生账号和信息泄漏 

#### 漏洞详情

[http://yjxt.bupt.edu.cn](http://yjxt.bupt.edu.cn )这个网站存在一个SQL注入漏洞。安全起见存在漏洞的地址就不贴出来了。同时欢迎有关老师私信索取地址，及时修复漏洞。接下来的事情很简单了，就是放到SQLmap里看看有什么有用的信息。表很多，没时间仔细找，暂时发现了部分学生学号和身份证号码等信息。这里就列出其中一个，并将学号、姓名、生日、身份证号打码。 

![2014-04-01-security-in-bupt-02-01](/images/2014-04-01-security-in-bupt-02-01.png)

那么接下来，如果有的同学一直在使用默认密码，也就是生日八位数字，那么意味着可以登录这个同学的账号。已经毕业的学生账号已经锁定，所以影响的是在校生。如果刚好是11级的，那么你甚至可以在照片信息核对这里看到女神的照片，而且是读研前与读研后的对比哦。 

![2014-04-01-security-in-bupt-02-02](/images/2014-04-01-security-in-bupt-02-02.png)

外包那边的开发人员找我帮忙调试，目前已经修复该漏洞。所以公布漏洞地址http://yjxt.bupt.edu.cn/Open/ExpertInfo.aspx?zjbh=2010810770

#### 原帖

[http://bbs.byr.cn/#!article/WWWTechnology/24215](http://bbs.byr.cn/#!article/WWWTechnology/24215)