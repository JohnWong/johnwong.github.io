---
layout: post
title: 跨平台移动开发与Hybrid学习笔记
category: mobile
description: 借React Native大热之际总结跨平台移动开发方案，学习典型Hybrid框架
thumb: /images/2015-04-20-cross-platform-and-hybrid.jpg
---

最近做了iOS平台上Hybrid的调研，水平有限，结合以前尝试Hybrid的一点点经验做个小小的分析。概述了跨平台开发的的各种方案，并通过阅读[Cordova-iOS]和[WebViewJavascriptBridge]的源码，分析Hybrid的实现原理和设计。

# 跨平台开发

这可能是移动开发领域的一个迷梦，无数人在用不同的方式想做好这一件事情，现在看起来还没有一套解决方案可以一统江湖。移动领域的跨平台开发可以从几个层面来切入（以下观点给予多年前的调研和最近的整理，出错了欢迎指出）。

####交叉编译

交叉编译是用一种语言开发，编译成不同平台的机器码。可以复用的是商业逻辑以及数据存取部分。典型代表是[Xamarin]，包含收费版和功能有限的免费版。使用C#作为开发语言，完成共享代码部分的编写，通过封装好的 C# API 来访问和操控Native UI。支持iOS，Android，Mac及Windows。除了提供IDE外还提供了云端测试、监控平台，非常有吸引力。

####编程语言翻译

将源编程语言翻译成不同平台的目标语言，实现一定程度上的代码复用。这类方案一般可以复用的是商业逻辑以及数据存取，适合逻辑复杂的应用。这样的解决方案有[J2ObjC]，免费开源。使用Java作为开发语言，在iOS平台翻译成OC。另外有Google Web Tookit可以将Java语言翻译为JavaScript，可以支持开发。实际应用可以阅读[Google Inbox如何跨平台重用代码？]，目前资源和成功示例还非常有限。Google放出了iOS示例项目[J2ObjC sample]问题多多，我还去提了个pull request。

####容器兼容 

同一种编程语言在多个平台运行，让容器成为语言和不同平台沟通的桥梁。这方面的先驱恐怕要数Java了吧，JVM完成了容器的作用。游戏平台普遍用这种这种方式，比如[Cocos2d-x]、[Unity]和[Corona SDK]。[Cocos2d-x]是用户最多的免费开源游戏开发平台，拥有发达的开发者社区。提供了C++和Lua API，支持iOS、Android、WinPhone 8, Windows, Mac OS X, Linux。[Unity]使用也非常广，提供了功能有限的免费版和收费版。[Corona SDK](https://coronalabs.com/)占有率较小，使用Lua作为开发语言，以前收费现在免费。另外还有[RubyMotion](http://www.rubymotion.com/)，用Ruby语言做跨平台开发。Ruby程序员的福音，但是价格略贵。

####Semi-hybrid App

介于Native和Hybrid之间，也类似于容器兼容，容器是JavaScript运行环境。使用JavaScript开发的同时提供原生界面，这样可以在享受Hybrid开发便利的同时提供原生的用户体验。这方面有[React Native](https://github.com/facebook/react-native)、[Native Script](https://www.nativescript.org/)、[Titanium]。React Native目前大热，支持iOS、Android和Web，目前只放出了iOS版。Native Script目前支持iOS、Android，Windows Phone在计划中。Titanium是一个老牌跨平台应用开发平台，支持Android、iOS 和Web。使用HTML、CSS、JavaScript开发，也支持PHP，Ruby和Python。当年在黑苹果上打开IDE点击运行，看到iPhone、Android和浏览器同时运行应用，内心还有点小激动呢。[BeeFramework]目前只支持iOS还不算跨平台，据说计划在1.0版本开始做跨平台。这里提到是因为他们最新的开发演示视频太酷了。

####Hybrid App

Hybrid App顾名思义，就是混合了Web和Native的开发方式。它本质上应用是一个WebView，大多数开发基于HTML、CSS和JavaScript，Native只是一个壳。这方面的平台有[PhoneGap/Cordova](http://phonegap.com/)、[Intel XDK](http://xdk-software.intel.com/)(原AppMobi XDK)和国内的产品[AppCan](http://www.appcan.cn/) 。有人会把Sencha Touch也列为Hybrid的一个平台。这样是不严谨的，实际上底层还是使用了Cordova来打包。

####Mobile Web

纯浏览器解决方案，对Native的能力使用十分有限。优点嘛，就是更新方便，无需安装。 


# Hybrid App

这种开发模式之所以出现是由于它有一些优点：

* 一次开发，多处运行
* 多平台一致的用户体验
* 学习和开发成本低
* 更新方便
* 适合内容展示类应用

当然，这种开发方式也有一些弊端：

* 用户体验不如针对平台的应用
* 性能和Native有差距
* 安全性差
* 不适合功能复杂的应用

我个人的理解是，Hybrid合理的应用场景是应用功能并不复杂，不苛求用户体验，人员和时间有限。 之前看到的一个例子是[ROR作者谈Hybrid开发](http://www.cocoachina.com/webapp/20141217/10667.html)，他们在开发37signal的Basecamp应用时通过Hybrid开发方式在已有的移动网站的基础上用1名程序员和1名设计师开发出了iOS 版本。目前应用由90% HTML +10%原生组成，会选择最值得做原生开发的那10%的部分来做原生开发。

我花了些时间挑选了两个比较有代表性的Hybrid项目，研究了它们的结构和实现细节。这两个项目分别是WebViewJavascriptBridge和Cordova-iOS。

## WebViewJavascriptBridge

[WebViewJavascriptBridge](https://github.com/marcuswestin/WebViewJavascriptBridge)是一个不错的JavaScript与Native之间双向通信的库，多个厂家包括Facebook在使用。项目结构简单，非常适合掌握Hybrid的实现原理。Native与JS间通信使用Web View来作为媒介。它们与Web View之间的交互放到了bridge层来处理，分别是Native Bridge和JS Bridge。首先需要学习的是Web View加载完成后Native给JS发消息的时序。可以分为3个阶段：

* Native发消息到Native Bridge

Native把要调用的JS的handler name和callback传给Native Bridge。Native Bridge会生成callback id，保存callback。

* Native Bridge发出消息，JS执行完毕通知Native Bridge

Native Bridge将消息（包含callback id和handler name）发到JS Bridge，JS Bridge根据handler name找到合适的handler并执行，执行完毕后将消息（包含callback id和结果）存到消息队列中，并通知Native Bridge。handler执行过程可能是异步的。

* Native Bridge从JS取回消息执行callback

Native Bridge从JS的消息队列中取回消息，并根据其中的callback id找到之前保存的callback，执行。

{% comment %} 
```sequence
Native->Native Bridge: call handler\nwith callback
Native Bridge->Native Bridge: generate id, save \ncallback and dispatch
Native Bridge->JS Bridge: handle message from ObjC
JS Bridge->JS: call handler
JS-->>JS: exec and callback
JS->JS Bridge: send result
JS Bridge->Web View: load ready request
Web View-->>Native Bridge: intercept ready request
Native Bridge->JS Bridge: fetch queue
JS Bridge->Native Bridge: message in queue
Native Bridge->Native Bridge: find callback by id
Native Bridge->Native: execute callback
```
{% endcomment %}
![Sequence1](//dn-johnwong.qbox.me/images/2015-04-20-cross-platform-and-hybrid-01.png)

上图中Native Bridge与JS Bridge间的消息发送是简化的，实际上都需要经过Web View。Native Bridge给JS Bridge发消息的关键方法是UIWebView的stringByEvaluatingJavaScriptFromString：

```
- (NSString *)stringByEvaluatingJavaScriptFromString:(NSString *)script;
```

JS Bridge给Native发消息时，将消息先保存，然后通过iframe加载一个特殊的url。Native Bridge拦截到这个url后，通过调用上面的stringByEvaluatingJavaScriptFromString方法来拿到消息。

如果是在Web View加载完成前发送消息，Native Bridge并不会立即发消息，而是将消息存到启动队列中。Web View在加载过程中，JS可以注册各种handler。加载完成后，Native Bridge将启动消息队列中的消息发出，之后的执行过程不变。时序图如下：

{% comment %}
```sequence
Native->Native Bridge: call handler\nwith callback
Native Bridge->Native Bridge: generate id,\nsave callback
Native Bridge->Native Bridge: save message to\nstartupMessageQueue
Native->Web View: load page
Web View-->JS Bridge: init
JS Bridge-->JS: bridge ready
JS->JS: register handlers
JS-->>JS Bridge:
JS Bridge-->>Web View:
Web View-->>Native Bridge: did finish load
Native Bridge->Native Bridge: dispatch messages in \nstartupMessageQueue
Native Bridge->JS Bridge: handle message from ObjC
JS Bridge->JS: call handler
JS-->>JS: exec and callback
JS->JS Bridge: send result
JS Bridge->Web View: load ready request
Web View-->>Native Bridge: intercept ready request
Native Bridge->JS Bridge: fetch queue
JS Bridge->Native Bridge: message in queue
Native Bridge->Native Bridge: find callback by id
Native Bridge->Native: execute callback
```
{% endcomment %}
![Sequence2](//dn-johnwong.qbox.me/images/2015-04-20-cross-platform-and-hybrid-02.png)

JS给Native发消息的过程非常类似：

{% comment %}
```sequence
Native->Native: register handler
Native->Web View: load page
Web View-->JS Bridge: init
JS Bridge-->>Web View:
note left of JS: JS给Native发消息
JS->JS Bridge: call handler\nwith callback
JS Bridge->JS Bridge: generate id, \nsave callback
JS Bridge->Web View: load ready request
Web View-->>Native Bridge: intercept ready request
Native Bridge->JS Bridge: fetch queue
JS Bridge->Native Bridge: message in queue
Native Bridge-->>Native Bridge: find handler by name\nand execute
Native Bridge->JS Bridge: handle message from ObjC
JS Bridge->JS Bridge: find callback by id
JS Bridge->JS: execute callback
```
{% endcomment %}
![Sequence3](//dn-johnwong.qbox.me/images/2015-04-20-cross-platform-and-hybrid-03.png)

这个库有一些值得注意的特性或者实现细节：

* Web View加载完成前，Native对JS的调用存储直到完成后发出
* webViewDidStartLoad可能执行多次，需要计数并在全部加载完成时处理启动队列
* 项目已经有兼容WKWebView和UIWebView的[pull request](https://github.com/marcuswestin/WebViewJavascriptBridge/pull/105)，并未合并到主干



## Cordova-iOS

这里有必要说一下Cordova和PhoneGap的关系。简单说来就是Cordova是PhoneGap的开源部分，PhoneGap是Cordova的发行版。有兴趣深入了解可以阅读[PhoneGap, Cordova, and what’s in a name?]。三年多前接过一个外包，要出Android和iOS两个版本，时间紧但用户体验要求不高。当时做选型，看过当时有的几个框架PhoneGap、Titanium、Corona SDK等，选择了学习成本最低开发最快的PhoneGap。最后也在很短时间内完成了开发。学习源码时我发现[Cordova-iOS]的源码中一些插件（比如定位、电池状态、联系人等）的实现放在了各自的库中。下载[PhoneGap]后打开其中的iOS 工程会看到加入各种插件后的源代码，学习起来更方便。Cordova有一些好的特色，值得学习：

#### 配置文件

应用的管理功能采用了配置文件（Android下为xml文件，iOS下为plist文件）。在配置文件中可以管理所有应用内使用的插件、日志级别、访问的ip白名单、开启历史记录等

#### 插件管理

Cordova将各种平台的一些原生功能封装成插件提供。新建应用的时候可以通过应用的配置文件指定使用哪些插件。一个典型的插件，比如设备信息可以参见[Cordova plugin device](https://git-wip-us.apache.org/repos/asf/cordova-plugin-device.git)。

建立一个插件的方法可以参考[PhoneGap 插件指南](http://docs.phonegap.com/en/edge/guide_hybrid_plugins_index.md.html)。这里简单介绍一下建立插件的方法。首先需要先定义一个插件配置文件`plugin.xml`，在其中指定各个平台的实现的源代码和使用这个功能的JS文件。在iOS平台，需要新建一个类继承`CDVPlugin`，定义一些方法供外部调用。在方法内调用其`commandDelegate`的`sendPluginResult`方法即可完成返回结果给JS。例如：

``` objc
- (void)getDeviceInfo:(CDVInvokedUrlCommand*)command
{
    NSDictionary* deviceProperties = [self deviceProperties];
    CDVPluginResult* pluginResult = [CDVPluginResult resultWithStatus:CDVCommandStatus_OK messageAsDictionary:deviceProperties];

    [self.commandDelegate sendPluginResult:pluginResult callbackId:command.callbackId];
}
```

在JS文件中定义这个插件的调用接口，即可在项目中使用：

```javascript
Device.prototype.getInfo = function(successCallback, errorCallback) {
    argscheck.checkArgs('fF', 'Device.getInfo', arguments);
    exec(successCallback, errorCallback, "Device", "getDeviceInfo", []);
};
```

#### 插件加载

读取配置文件后并不立即初始化插件。在首次使用时初始化并保存到字典中。遇到内存警告时回收插件。

#### 白名单

白名单功能控制允许加载的schema、域名或者IP、URL path，支持wildcard通配。web view发出的请求如果的scheme是http/https/ftp/ftps，并且符合白名单规则的用web view打开。如果scheme是gap，则触发Native从JS环境中获取任务队列。这一点与WebViewJavascriptBridge很类似。

#### 多种JS调用Native模式

Cordova支持多种JS向Native发送信息的模式：

* IFRAME_NAV
* XHR_NO_PAYLOAD
* XHR_WITH_PAYLOAD
* XHR_OPTIONAL_PAYLOAD
* IFRAME_HASH_NO_PAYLOAD
* IFRAME_HASH_WITH_PAYLOAD
* WK_WEBVIEW_BINDING

各种模式的限制和对比可以参见[exec.js源代码](https://github.com/apache/cordova-ios/blob/master/cordova-js-src/exec.js)。`IFRAME_NAV`模式是最快的。由于这种模式存在一些问题，目前默认的发送消息方式改为`XHR_OPTIONAL_PAYLOAD`。参见[修改JavaScript到Native的桥接模式](https://github.com/apache/cordova-ios/blob/3.9.x/guides/Changing%20the%20JavaScript%20to%20Native%20Bridge%20Mode.md)

[PhoneGap, Cordova, and what’s in a name?]:http://phonegap.com/2012/03/19/phonegap-cordova-and-what%E2%80%99s-in-a-name/ 
[Cordova-ios]:https://github.com/apache/cordova-ios 
[WebViewJavascriptBridge]:https://github.com/marcuswestin/WebViewJavascriptBridge
[Google Inbox如何跨平台重用代码？]:http://coolshell.cn/articles/12136.html 
[J2ObjC]:https://github.com/google/j2objc
[J2ObjC sample]:https://github.com/tomball/j2objc-sample-reversi 
[Xamarin]:http://xamarin.com/
[Cocos2d-x]:http://www.cocos2d-x.org/
[BeeFramework]:https://github.com/gavinkwoe/BeeFramework
[Titanium]:http://www.appcelerator.com/titanium/
[Unity]:http://unity3d.com/
[Corona SDK]:https://coronalabs.com/products/corona-sdk/
[PhoneGap]:http://phonegap.com/