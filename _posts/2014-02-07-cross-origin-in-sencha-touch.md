---
layout: post
title: "Sencha Touch跨域问题解决"
category: past
description: 解决跨域问题
---
之前对于跨域问题仅有粗浅的认识，一般是浏览器层面出于安全性的考虑，不允许调用其他页面的对象。这次在Sencha Touch中解决这个问题额外花掉不少时间。

解决的方法大概就是：

1. 修改服务器的header；
2. JsonP。JsonP方法是一种非官方的解决方案，只支持Get方法，需要服务器端根据callback参数返回不同的内容。返回的内容不是标准的json&#26684;式，对服务器端的改动会比较麻烦。我选择了修改服务器返回的header的方法。

#### 1. 修改header的Access-Control-Allow-Origin
将header的Access-Control-Allow-Origin设为允许的域名列表，我这里直接设置为星号了。项目采用的是SSH的架构。在jsp文件中，可以使用response.addHeader方法修改header，在所有页面都会包含的公共文件中加入即可。更好的办法是写一个Filter，对json请求的路径拦截，修改header：

```java
HttpServletResponse httpResponse = (HttpServletResponse)response;
		httpResponse.addHeader("Access-Control-Allow-Origin", "*");
```

对于iframe跨域的问题，可以将设置“P3P"为"CP=CAO PSA OUR"。

#### 2. 修改header的Access-Control-Allow-Headers
在新版的Chrome浏览器下，上述方法仍然无法达到目的，需要将header的Access-Control-Allow-Headers设为Origin, X-Requested-With, Content-Type, Accept。

#### 3. 修改Sencha Touch

一般情况下跨域问题已经解决了。在Sencha Touch下发现每一个Ajax请求都发送了两次，其中一次的请求方法为OPTIONS。我只知道常用的Get、Post，听说过Put、Delete。查过后才知道OPTIONS方法是用于获取指定URL能接收的请求方法。我用jQuery发送GET请求没有出现，手写HttpXmlRequest也没有出现。这样的问题在StackOverFlow和Sencha论坛上也看到有不少人遇到。用Web调试工具找发送OPTIONS请求的地方，没有找到。对于jQuery和Sencha的http请求头，发现了问题所在。Sencha发送的头中包含了X-Requested-With的头，jQuery中没有。估计是这个请求头触发了浏览器去探测该URL可用的请求方法。大多服务器都不支持这个方法，觉得Sencha这么做是多此一举了。如果是使用Ext.Ajax.request发送请求，直接在配置中写useDefaultXhrHeader
 : false就可以了。但是这里是将请求用在Ext.data.Store中，不支持这个配置。懒得该太多源文件支持这个配置，直接将Connection.js中这个配置的默认&#20540;改为false。

另外还遇到Sencha Touch编译的坑。特定版本编译报Logger.js不存在，需要将app.json中的buildOptions下logger的&#20540;由"no"改为"false"。接下来需要解决的sencha touch的坑是开发环境运行问没问题，编译后界面部分不显示，交互出问题。

感谢IBM实习的机会，让我学会了Web调试。感谢万能的StackOverFlow，能找到各种问题的解决方案。

