---
layout: post
title: "扒一扒北邮的安全问题[1]-学生收费查询系统"
category: past
description: 毕业前把自己无聊玩的抖出来。
thumb: /images/2014-03-31-security-in-bupt-01-02.png
---

#### 漏洞类型： 

登录绕过/SQL注入

#### 相关网站

财务处学生收费查询系统

#### 问题描述

登录存在SQL注入漏洞导致学生姓名和交费信息泄漏

#### 漏洞详情

`http://10.100.52.251/search/xssf/xssf.htm`这个网站有三个模块，第一个学生个人收费查询暂时没有找到破解方法。 
第三个模块管理员入口，用户一栏填写经典的登录绕过'or'='or'，成功绕过登陆。 

![2014-03-31-security-in-bupt-01-01.png](//dn-johnwong.qbox.me/images/2014-03-31-security-in-bupt-01-01.png)

![2014-03-31-security-in-bupt-01-02.png](//dn-johnwong.qbox.me/images/2014-03-31-security-in-bupt-01-02.png)

看到了一大批账号，例如gl_gy。 
再来到第二个模块系部查询，用户一栏填写gl_gy'or'，成功以公寓的账号登录系统，能够查询到学生交费信息。 

![2014-03-31-security-in-bupt-01-03.png](//dn-johnwong.qbox.me/images/2014-03-31-security-in-bupt-01-03.png)
  
PS. lz是刚毕业的菜硕，非安全专业的，课余时间搞搞，发现好多有意思的事情分享给大家，同时也希望大家能够重视安全问题。 

#### 原帖

[http://bbs.byr.cn/#!article/WWWTechnology/24212](http://bbs.byr.cn/#!article/WWWTechnology/24212)