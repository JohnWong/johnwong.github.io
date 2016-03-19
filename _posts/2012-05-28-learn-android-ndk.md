---
layout: post
title: "Android NDK学习记录"
category: past
description: 游戏项目开始转向Cocos2d-x来开发。硬着头皮开始学习。
---
游戏项目开始转向Cocos2d-x来开发。需要用什么NDK、cygwin。硬着头皮开始学习。

1. 下载NDK，最新版r7。解压到D:\Develop，地址如下：http://dl.google.com/android/ndk/android-ndk-r7-windows.zip

2. 项目的native代码放在 `<project>/jni/...`

3. 创建 `<project>/jni/Android.mk` 描述navive代码。

4. 编译native代码：
``` 
 cd <project> 
<ndk>/ndk-build
```
5. 程序中的类内加载编译好的.so文件使用代码：

```
static { 
  System.loadLibrary("hello-jni"); 
}
```
用到的方法在类中使用示例:

```
public native String  stringFromJNI();
```

6.android-ndk-r7\samples\下有示例代码，hello-jni运行成功。

Cygwin下编译native代码只是第四步有所不同。需要安装Cygwin的以下包：

```
autoconf2.1
automake1.10
binutils
gcc-core
gcc4-core
gdb
pcre
pcre-devel
GNU awk
```

在D:\cygwin\home\Administrator\.bash_profile添加：

```
NDK=/cygdrive/d/Develop/android-ndk-r7
export NDK
```

进入Cygwin Bash，进入项目目录，用$NDK/ndk-build即可编译native代码。 常见错误参见http://www.chinavideo.org/archiver/?tid-10821.html

ndk试验成功，万里长征第一步，接下来配置cocos-2d。
