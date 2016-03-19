---
layout: post
title: "bat实现IP切换"
category: past
description: 出差调试设备，需要在几个网段之间切换，因此做了个bat实现快速切换。
---
出差调试设备，需要在几个网段之间切换，因此做了个bat实现快速切换。

```bash
@echo off
set nic="本地连接"
set num=151
set /p choice="输入0切换为自动获取，输入1切换到外网，输入2切换到192.168.20.%num%，输入3切换到192.168.0.%num%:"
if "%choice%"=="0" goto C0
if "%choice%"=="1" goto C1 
if "%choice%"=="2" goto C2
if "%choice%"=="3" goto C3
goto END
:C0
echo 开始设置自动获取IP
netsh interface ip set address "%nic%" dhcp
goto END
:C1
echo 切换到外网...
netsh interface ip set address "%nic%" static 192.168.24.%num% 255.255.255.0 192.168.24.1
netsh interface ip add dns name="%nic%" addr=8.8.8.8
echo 已经切换到外网
goto END
:C2
echo 切换到20网段
netsh interface ip set address "%nic%" static 192.168.20.%num% 255.255.255.0
echo 已经切换到20网段
goto END
:C3
echo 切换到0网段
netsh interface ip set address "%nic%" static 192.168.0.%num% 255.255.255.0
echo 已经切换到0网段
goto END
:END
pause
```





