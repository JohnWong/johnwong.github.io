---
layout: post
title: "MySQL编码、Spring配置中编码、Struts中文问题"
category: Past
description: 今天遇到的中文编码有关的三个问题，包括MySQL、Spring和Struts。
---

今天遇到的编码有关的三个问题

1. mysql存入和去除的数据乱码，原因是新建的数据库不支持中文，修改数据库编码为GBK或者UTF-8

2. spring中配置数据连接，需要在jdbcUrl中指明数据编码：

```
jdbc:mysql://127.0.0.1:3306/auction?useUnicode=true&characterEncoding=gbk
```

需要注意的是这个xml文件中不能直接使用&，而需要使用转移后的&

3. Struts中使用中文编码建议选utf-8，原因是ajax等，如果使用GBK会费一番周折，参见[当AJAX遭遇GBK的尴尬](http://www.blogjava.net/errorfun/archive/2006/12/30/91000.html)与[struts中文问题解决方案](http://blog.csdn.net/feng_sundy/article/details/139647)。

UltraEdit对各种编码处理不好，Notepad++处理的非常好，大多数情况编码都能识别正确，还能自由转换。遇到不知道编码格式的用Notepad++打开就可以了解了