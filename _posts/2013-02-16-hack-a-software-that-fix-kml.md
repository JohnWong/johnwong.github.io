---
layout: post
title: "某kml纠偏软件数据破解"
category: past
description: 为了提高纠偏数据库的准确性，破解了一款kml纠偏软件拿到了数据库。
---

最近想写个谷歌地图纠偏软件，一是网上可以的不多，各种软件都是超过三次收费或者文件超过某尺寸收费。用Python写了个读取kml并就纠偏的小程序，运行没问题，但是最大的问题在于纠偏数据库的准确性。我用的一个感觉准确性一般，找到超过尺寸收费的某纠偏软件，于是想破解一下参考纠偏数据。

发现解压后有一些隐藏文件，其中最大的dat.dm是数据无疑，修改扩展名为rar，打开失败。修改为zip提示需要密码。同时发现有dat.db，修改扩展名为exe后运行，原来这个是unrar程序。明显是用这个来解压之前的zip包的。unrar的参数中带入压缩包密码，思路就是自己写一个程序替代这个unrar，把接收到的参数写入文件，密码就一目了然了。早就卸载了笨重的VS，于是打开从考研复试后就没用过的devcpp，程序很简单，但是一年半没摸C语言，还是得找度娘帮帮忙才完成。

替换掉程序后运行纠偏软件，结果卡住好长时间不动。结束卡住的进程，然后报错找不到C:\Users\XXX\AppData\Local\Temp\Mars2Wgs.txt。Mars2Wgs.txt应该就是解压后的数据文件。这时想到另一个方法，直接取得解压后的数据文件。这个文件是每次运行完程序就会删除掉。尝试系统设置禁止删除该文件，失败。然后尝试把程序纠偏后输出的文件去掉所有权限。这样程序会报错，如果删除数据文件的代码在写入输出文件之后那么就不会删除掉数据文件了。 这样成功得到了数据文件。

没有搞到解压密码多少不爽。于是沿着第一个方法摸索。发现是自己程序写的有问题。文件写入后忘记关闭文件了。修改好后取得了解压密码。

现在最烦的是搞到数据文件，分析格式。WTF完全比较晕。