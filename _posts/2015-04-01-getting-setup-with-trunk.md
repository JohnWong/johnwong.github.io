---
layout: post
title: "开始建立你的trunk"
category: mobile
description: 等待提交CocoaPod的时候顺带翻译了帮助文档
thumb: /images/2015-04-01-getting-setup-with-trunk.png
---

本文翻译自[Getting Setup With Trunk](http://guides.cocoapods.org/making/getting-setup-with-trunk.html)。等待提交CocoaPod的时候顺带翻译的。夜间翻墙速度飞起，很顺利地完成了提交。打开官方Specs网站你会发现所有的commit都是由机器人[CocoaPodsBot](https://github.com/CocoaPodsBot)代为提交的。这机器人还有6个follower。你如果闲的慌可以订阅这个账号的feed，估计会被最新Specs各种刷屏。CocoaPods用得越多，越觉得很灵活有意思。顺带推荐下我维护的Specs库的[Gitcafe镜像](https://gitcafe.com/yellowxz/Specs)，不定期更新。

## 关于trunk我需要知道什么

CocoaPods trunk是一个授权和CocoaPods API的服务。如果要提交库到CocoaPods，你将不得不在一台设备上注册并拥有会话。你可以在[这个博客](http://blog.cocoapods.org/CocoaPods-Trunk/)上阅读一点关于它的历史和开发过程。

从CocoaPods 0.33开始，我们在`pod trunk`下有了一些命令来处理你的Podspecs的自动化部署和管理。你可以在任何时候运行`pod trunk [command] --help`来得到内置的帮助。

## 开始

我们首先用命令`pod trunk register`注册一个账户，可以把这看成是注册一个设备而非一个用户账户。

我们推荐使用完整的命令来为随后你查看自己的绘画提供一些上下文，比如：

> $ pod trunk register orta@cocoapods.org 'Orta Therox' --description='macbook air'

随后你的电子邮件地址将会收到一封邮件来验证当前电脑与你的trunk的账户之间的关联。你可以通过运行`pod trunk me`来查看你的会话。

你并没有一个密码，只有一个每台电脑一个的会话token。

## 部署库

在带有Podspec的库的目录下运行`pod trunk push`————需要注意的是这与私有pod repo的`pod push`不同。这将会：

* 在本地校验你的Podspec
* 在校验成功后将Pod转换成JSON推到trunk
* trunk将会为你的库生成规范的JSON表示

一旦库被添加，trunk将会提交一个web钩子到其他服务来通知它有新的CocoaPod，比如[CocoaDocs.org](http://cocoadocs.org/)。

## 添加其他人作为贡献者

对于有多个维护者的库，推第一个版本的第一个人可以使用命令`pod trunk add-owner`来添加其他维护者，比如要添加`kyle@cocoapods.org`到我的库`ARAnalytics`，我会运行：

> $ pod trunk add-owner ARAnalytics kyle@cocoapods.org

接下来这将会列出所有已知的库拥有者。

## 声索现有的库

如果你希望声索一个别人已经宣称拥有的库，那么你可以使用[我们的声索表格](https://trunk.cocoapods.org/claims/new)来表达你是一些库的维护者/拥有者。任何关于库所有权的问题交由CocoaPods开发团队仲裁。
