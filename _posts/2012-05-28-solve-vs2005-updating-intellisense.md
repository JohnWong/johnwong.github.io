---
layout: post
title: VS2005 "正在更新 IntelliSense"无法通过的解决办法
category: Past
description: 在使用完一段时间VS2005之后，发现不能打开类向导，一直提示“正在更新IntelliSense"
---

在使用完一段时间VS2005之后，发现不能打开类向导，一直提示“正在更新IntelliSense"

找了网上的代码，所有的答案都是关于：把feacp.dll文件删除或者改名。但这样的代价就是无法使用用类视图快速定位代码。

注销用户之后，发现另外一个用户的环境竟然可以打开。于是想到将VS的环境重置一下。关闭VS2005之后，在命令行下输入命令

```
x:\Program Files\microsoft visual studio 8\common7\ide\devenv.exe" /setup /resetuserdata /resetsettings
```

`x:\Program Files\microsoft visual studio 8\common7\ide\devenv.exe`为VS的安装目录。执行需要几分钟。完毕后将目录重新包括一下。一切OK。