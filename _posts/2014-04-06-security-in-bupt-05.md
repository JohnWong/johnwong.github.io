---
layout: post
title: "扒一扒北邮的安全问题[5]-教务账号外泄到鲜次元"
category: Past
description: 毕业前把自己无聊玩的抖出来。
thumb: /images/2014-04-06-security-in-bupt-05-01.png
---

#### 漏洞类型： 

SQL注入

#### 相关网站

鲜次元

#### 问题描述

鲜次元网站存在sql诸如漏洞，其数据库存储这部分同学的教务账号

#### 漏洞详情

之前就发现鲜次元网站存在sql注入漏洞，搞到了mysql的root账户加密后的密码，一直无法解密。今天闲来无事进一步测试，发现其中有一个数据库名为a1015151118，里面的user表存储这用户信息，但是存在password、xuehao、byrpassword和jwcpassword。惊呆了，莫非包含了学号、北邮人密码和教务处密码。用户的北邮人账号不清楚，所以北邮人密码也用不上，就试试教务处网站。 
password字段是加密的但是有部分可以简单解出来。学号已经有了，jwcpassword字段好多是空的，就用password字段解密后作为教务处密码。试了几个账号，有一个成功了，而且还是朝鲜族美女。后面又成功登录了几个账号，懒得继续试下去了。 

![2014-04-06-security-in-bupt-05-01.png](//dn-johnwong.qbox.me/images/2014-04-06-security-in-bupt-05-01.png)

PS. 后来了解到鲜次元为一个校内活动提供数据库支持但是活动结束后没及时清理数据才会有学生信息。没想到现在鲜次元独立网站已经关掉，切换到新浪博客上也许久没更新了，应该是阵亡了，挺可惜的。

#### 原帖

[http://bbs.byr.cn/#!article/WWWTechnology/24483](http://bbs.byr.cn/#!article/WWWTechnology/24483)