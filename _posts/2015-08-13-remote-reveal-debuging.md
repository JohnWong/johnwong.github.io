---
layout: post
title: 跨网段使用Reveal调试
category: mobile
description: 找到了跨网段使用Reveal调试的方法，然而并没有用到
thumb: /images/2015-08-13-remote-reveal-debuging.png
---

Reveal是iOS开发中经常用到的调试利器。在公司使用中遇到了无法找到设备的问题。因为Reveal使用Bonjour来完成设备服务发现，但是在公司内手机和Mac常常不在同一个网段内，会出现无法找到设备的问题。花了些时间来解决这个问题，挺有意思的。

## Reveal通信方法

想了解手机上Reveal的库与Mac上客户端的通信方法，找到了一篇官方帮助文档很有价值：[Bonjour Debuging](https://support.revealapp.com/hc/en-us/articles/360022667731-Bonjour-Debugging-Why-can-t-I-connect-to-my-app-)。这里我们知道了服务发现用的是Bonjour，下面是一些有用的方法：

获取周围所有reveal服务列表

```
dns-sd -B _reveal._tcp local
```

运行之后会列出一些服务列表。在某一条信息中，拿到实例名称，可以根据实例名称查询主机名与端口号。reveal同时还会返回一些设备信息、应用信息与reveal协议版本号。

```
dns-sd -L Reveal--618e4d6a _reveal._tcp.
```

Reveal使用的是HTTP协议，将从Bonjour拿到的主机名与端口拼接起来，就可以查看Reveal的协议，并未加密。

```
http://johns-5s.local.:65152/application
```

通过抓包分析Reveal协议使用的URL除了`/Application`外还有`/objects/188?subviews=0`。

## 打通网段

### 请求转发

想要打通网段，想到的第一个方法是写代理应用来转发。首先是通过Bonjour来发布一个Reveal服务，使用`NSNetService`来实现。我发现Reveal设备列表里显示的应用和设备信息并不通过Reveal自己的HTTP接口获取，而是通过Bonjour来提供的。这些信息可以通过`- (BOOL)setTXTRecordData:(NSData *)recordData;`方法来设置。可以通过`+ (NSData *)dataFromTXTRecordDictionary:(NSDictionary *)txtDictionary`方法将一个字典转换成这里要用的NSData。

建立NSNetService需要提供一个端口。起初对Bonjour的作用并不是很理解。当时随便写了一个。在使用这个端口进行HTTP请求的时候，在NSNetService中并不能找到响应的方法。直到阅读了CocoaHTTPServer的代码后，才明白Bonjour只是帮你把服务公布出去，并不涉及服务建立。

因此使用CocoaHTTPServer建立HTTP服务来响应请求，将一些Bonjour用到的信息设置进去，CocoaHTTPServer会自动帮你发布。这个方法是行得通的，Reveal会正常加载。过程中唯一遇到的问题是Reveal应用会判断HTTP头的Content-Type，写成`application/json; charset=utf-8`。

接下来需要做的是拿到设备的主机名与端口，转发请求。在做这些事情之前，我想到了另一个方法。

### Bonjour转发

忽然想到网络本身是可以通信的，只是Bonjour没能跨网段。只要在本地建立一个Bonjour服务，并在收到查询的时候将设备的IP、端口等信息返回就可以了。这件事情甚至在命令行就足以完成：

```
dns-sd -P Reveal--0a260b700000 _reveal._tcp local 50757 xx.xx.xx.xx xx.xx.xx.xx  "devLocalModel=iPhone" "isSim=false" "devName=Proxy John's 5S" "appName=RevealIt" "devSysVer=9.0" "devSysName=iPhone OS" "appBundleId=com.johnwong.RevealIt" "protoVer=18"
```

为了防止这个服务与设备原有的服务冲突，在实例名称后添加了4个0，主机名也使用IP地址。

接下来需要做的就是获取设备中一些信息用来建立Bonjour服务。建立了项目[Reveal Proxy](https://github.com/JohnWong/reveal-proxy)来做这些事情，只需要将Bonjour目录下代码加入项目。加入后将会打印出需要在命令行输入的命令，就可以在Reveal中调试设备了。

```
Bonjour
├── JWBonjour.h
├── JWBonjour.m
├── JWBonjourManager.h
├── JWBonjourManager.m
├── JWBonjourUtil.h
└── JWBonjourUtil.m
```

```
2015-08-13 17:13:33.104 RevealIt[12647:562110] Bonjour Run:
dns-sd -P Reveal--0a260b700000 _reveal._tcp local 50757 xx.xx.xx.xx xx.xx.xx.xx  "devLocalModel=iPhone" "isSim=false" "devName=Proxy John's 5S" "appName=RevealIt" "devSysVer=9.0" "devSysName=iPhone OS" "appBundleId=com.johnwong.RevealIt" "protoVer=18"
```

最最后想说的是，解决了这个问题后，发现目前手机与Mac不在一个网段，也能发现设备。也就是说搞完了发现并没有什么用处。唉，有空再看看Reveal的协议，看看能做点什么。

## Reference

[Bonjour开发资源](https://developer.apple.com/bonjour/)