---
layout: post
title: 在Terminal使用socks5代理
category: mobile
description: Terminal也需要科学上网
thumb: /images/2015-10-29-using-sock5-in-terminal.jpg
---
平时用SSLedge科学上网，速度很不错。在公司有时候连不上，不过这主要是公司破网络的问题。开发中经常需要在Terminal做一些事情，比如使用github、更新gem、安装brew等等。平时的使用中很慢，而且有些开发网站被屏蔽，这就需要Terminal也能科学上网。

## 一个sock5代理

首先你要有一个sock5代理。我使用的是[https://eurekavpt.com/](https://eurekavpt.com/)。安装和配置参考网站的文档。建立sock5代理的方法是在GoAgentX中新建一个SSLedge服务，选择带✧的服务器，并勾选Socks Mode。记住它的端口，比如我使用的是8032。

## proxychains的安装与配置

在Terminal中使用代理的一个非常棒的工具是proxychains。在Mac平台下名称叫做proxychains-ng，可以通过Homebrew安装：
```
brew install proxychains-ng
```

配置文件路径为`/usr/local/Cellar/proxychains-ng/4.10/etc`，配置最后部分修改为：

```
[ProxyList]
socks5 	127.0.0.1 8032
```

## 使用方法

确保你的GoAgentX中sock5代理已经启动。在Terminal中需要使用代理的命令前面加`proxychains4`就可以了。例如clone一个git库：

```
proxychains4 git clone https://github.com/JohnWong/johnwong.github.io.git
```

拯救你的开发，简直就是飞一般的感觉。像CocoaPods的Specs这样庞大的代码库也不在话下，曾经达到近10MB/s的速度，简直震惊。