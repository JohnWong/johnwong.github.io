---
layout: post
title: "端口占用问题"
category: past
description: 查看占用指定端口的进程
---
查看占用制定端口的进程

netstat -aon|findstr "9050"TCP &nbsp; &nbsp;127.0.0.1:9050 &nbsp; &nbsp; &nbsp; &nbsp; 0.0.0.0:0 &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;LISTENING &nbsp; &nbsp; &nbsp; 2016

查看该进程

tasklist|findstr "2016"tor.exe &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 2016 Console &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; 0 &nbsp; &nbsp; 16,064 K



