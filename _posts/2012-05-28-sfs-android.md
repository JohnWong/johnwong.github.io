---
layout: post
title: "SFS&Android——Android例程调试"
category: Past
description: 自己写了个SFS的Java客户端的测试程序，消息收发都没用问题，转而进军Android。这回真是费好大劲了，断断续续debug三四天了。
---
自己写了个Java客户端的测试程序，消息收发都没用问题，转而进军Android。这回真是费好大劲了，断断续续debug三四天了。

Android的BasicServerConnection例程总是运行出错，出错的地方是jar包中的方法不是自己写的方法。冥思苦想一天不得其解。只能自己写了个小程序开始测试SFS在Android中的使用。首先测试连接，翻出毕业设计的服务器端。结果始终连不上服务器，调试一天才发现Android项目忘记加网络访问权限了。巨汗无比下班回家去了。

然后证明了SFS客户端可以访问服务器，但是依然是出错。最后拜谷歌大神的site搜索，才终于找到了问题所在。就在SFS论坛的不起&#30524;的帖子里版主贴出了常见问题。我愤慨！为毛官网API里面不说一下，代码里说一下也行啊，害我折腾这几天。帖子如下：&nbsp;http://www.smartfoxserver.com/forums/viewtopic.php?t=10370&sid=e8738ca6731e59edf8241634fbef69b4&nbsp;&nbsp;

http://www.smartfoxserver.com/forums/viewtopic.php?t=10370&sid=e8738ca6731e59edf8241634fbef69b4

这是篇神贴，里面说的三个常见问题我都遇到了。1.Android网络访问权限。2.127.0.0.1不是Android模拟器的本地地址，而应该是10.0.0.2。3.Android客户端默认使用IPv6。要使用IPv4需要加语句：

System.setProperty("java.net.preferIPv6Addresses", "false");

