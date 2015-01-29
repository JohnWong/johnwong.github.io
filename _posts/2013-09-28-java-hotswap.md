---
layout: post
title: "Java Hotswap"
category: Past
description: 小例子来了解Java的Hotswap原理。
---
Link: [http://www.ibm.com/developerworks/cn/java/j-lo-hotswapcls/](http://www.ibm.com/developerworks/cn/java/j-lo-hotswapcls/)

Download: [http://download.csdn.net/detail/yellowxz/6331851](http://download.csdn.net/detail/yellowxz/6331851)

Hotswap简单说来就是实现自定义的ClassLoader，载入类的时候使用自定义的ClassLoader。覆写loadClass方法，在其中动态载入最新的类。

缺点是Hotswap只能使新创建的类是最新的，但是对于已经在运行的类无法实现替换。这看起来是个不可能完成的任务。欢迎指教。