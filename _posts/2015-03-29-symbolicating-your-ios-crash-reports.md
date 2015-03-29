---
layout: post
title: "符号化你的iOS崩溃报告"
category: Mobile
description: 做完小工具就发烧，意识模糊的情况下翻译的。。。
---

## 前言

本文翻译自[Symbolicating Your iOS Crash Reports](http://possiblemobile.com/2015/03/symbolicating-your-ios-crash-reports)。这是一篇对于iOS崩溃报告符号化的比较全面的文章。我对`Symbolicatecrash`工具做了比较完善的封装，一句话就可以符号化你的崩溃报告，还集成了检查UUID匹配的功能。

```
sh symbolicate.sh Crasher.crash Example/Crasher.app > Crasher_Symbolicated.crash
```

或者

```
sh symbolicate.sh Crasher.crash Example/Crasher.app.dsym > Crasher_Symbolicated.crash
```

项目地址：[https://github.com/JohnWong/symbolicate](https://github.com/JohnWong/symbolicate)

## 准备开始

你一定已经处理过你的app的崩溃报告，但是其堆栈回溯包含难以辨认的内存地址。作为一个开发者该怎么办呢？简单说来，你需要将调试符号应用在堆栈追踪上使其可读，这个过程被称作符号化。

但是在我们准备开始之前，你可以使用[Crasher](https://github.com/chaledoubleencore/Crasher)，它提供了一个示例崩溃报告让你来解码。

你应该有`.crash`文件。如果没有，你可以从iTunes Connect上获取，通过Xcode（Window > Devices）直接从链接的设备上获取，从连接的设备（Settings > Privacy > Diagnostics & Usage），或者亲自动手使用PLCrashReporter框架。你可能已经使用第三方崩溃报告服务，它将会在你正确设置后为你符号化崩溃报告。

依赖于你的app的构建如何配置，你需要下列文件中一个或者两者都需要：

* 崩溃的应用构建的`.app`。包里包含了app的二进制，可能包含了调试符号。（如果你有一个`.ipa`，你可以把它当作一个`.zip`文件来解压出其中的`.app`。）
* 崩溃的应用构建的`.dSYM`。如果你的`.app`不包含调试符号，这将是你的应用的包含调试符号的副产品。

你需要哪一个？在Xcode里，在构建设置中寻找“Strip Debug Symbols During Copy”（COPY_PHASE_STRIP）。当启用时，调试符号将会在你的`.app`中省略，并放置在一个`.dSYM`文件中。否则你的`.app`包含了这些符号。（为了混淆，调试符号在release构建中默认剥离。你大概不应该修改release配置的设置。）

## 但是等一下，什么是调试符号？

在我们的用途下，一个调试符号是一个程序员给一个方法所取的可读的名字。编译器通过减少这些命名的调试符号到其自身的符号来混淆代码。你不能指望这些符号在两次构建后相同，即使是你构建相同的代码两次。

## 检查Crash

如果你通过Xcode的Organizer从设备拉取到崩溃日志，你的崩溃报告可能自动符号化UIKit或者其他iOS框架。如果你的Xcode仍然了解你的构建，它将会自动符号化你的崩溃报告。

如果不是这种情况，那么你需要自己来符号化。

## 使用“Symbolicatecrash”工具来符号化

幸运的是Apple提供给我们一个脚本来检索调试符号并应用到崩溃报告上。

对于Xcode 6来说，你可以在这里找到：
`/Applications/Xcode.app/Contents/SharedFrameworks/DTDeviceKitBase.framework/Versions/Current/Resources/symbolicatecrash`

或者如果你在使用Xcode 5：
`/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/Library/PrivateFrameworks/DTDeviceKitBase.framework/Versions/Current/Resources/symbolicatecrash`

为了使用这个工具，你需要导出`DEVELOPER_DIR`环境变量到你的Xcode安装目录的合适的路径：

> export DEVELOPER_DIR="/Applications/Xcode.app/Contents/Developer"

将你的`.crash`，`.app`和`.dSYM`文件放在同一个目录下并运行：

> symbolicatecrash -v ScaryCrash.crash > Symbolicated.crash

你可能需要制定app的二进制：

> symbolicatecrash -v ScaryCrash.crash ./Crasher.app/Crasher > Symbolicated.crash

如果你在使用[Crasher](https://github.com/chaledoubleencore/Crasher)的示例中方便的脚本，可以省略verbose标记：

> sh symbolicate6.sh ScaryCrash.crash ./Crasher.app/Crasher > Symbolicated.crash

## 验证你的符号化

如果符号化并不起效，再次检查你拿到的是正确的`.dSYM`和`.app`。你可以通过对比崩溃报告中构建的UUID和app二进制中的UUID来再次检查：

> dwarfdump –uuid Crasher.app/Crasher

>UUID: __B00CDF0C-2965-3095-B1E8-6078B12D79E5__ (armv7) Crasher.app/Crasher
UUID: 3F3BE3C6-DD2E-3E23-A603-A18097C9317F (arm64) Crasher.app/Crasher

并且在dSYM中：

>dwarfdump –uuid Crasher.app.dSYM/Contents/Resources/DWARF/Crasher

>UUID: __B00CDF0C-2965-3095-B1E8-6078B12D79E5__ (armv7) Crasher.app.dSYM/Contents/Resources/DWARF/Crasher
UUID: 3F3BE3C6-DD2E-3E23-A603-A18097C9317F (arm64) Crasher.app.dSYM/Contents/Resources/DWARF/Crasher

对于崩溃报告中的UUID：

>0xa8000 – 0xaffff Crasher armv7 &lt;__b00cdf0c29653095b1e86078b12d79e5__&gt; /var/mobile/Containers/Bundle/Application/956755E3-6C66-4E87-A8BC-352FD4BE3711/Crasher.app/Crasher

`symbolicatecrash`工具的verbose日志也列出了其发现的UUID。

## “Symbolicatecrash”工具故障排除

如果你仍然感到困惑，小心检查符号化的日志。符号化工具试图通过匹配你的app和其他动态框架的UUID来定位到合适的文件。查找你的app名称或者UUID来看是否匹配。

> …….fetching symbol file for Crasher[K–[undef]
Searching []…– NO MATCH
Searching in Spotlight for dsym with UUID of b00cdf0c29653095b1e86078b12d79e5
...
Number of symbols in /Users/You/Workspace/Crasher.app/Crasher: 1 + 106 = 107
Found executable /Users/You/Workspace/Crasher.app/Crasher
– MATCH

这里有一个你可能遇到的Spotlight无法定位到你的`.dSYM`的日志的示例：

> Did not find executable for dsym
Warning: Can't find any unstripped binary that matches version of /private/var/mobile/Containers/Bundle/Application/956755E3-6C66-4E87-A8BC-352FD4BE3711/Crasher.app/Crasher

或者其他无效输入：

>fatal error: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/lipo: can't figure out the architecture type of: ./Crasher.app.dSYM.zip
./Crasher.app.dSYM.zip doesn't contain armv7 slice

Xcode 6版本的`symbolicatecrash`工具尝试修复一些Xcode 5版本所面对的Spotlight问题。如果你仍然有麻烦，它可能是一个Spotlight的文件索引问题。试试：

>mdimport -g /Applications/Xcode.app/Contents/Library/Spotlight/uuid.mdimporter .

## 使用命令行工具链

我们可以更深入一步，使用开发者工具链来一行一行地符号化堆栈追踪的内存地址。如果你以前使用这种方法遇到了很大麻烦，可能是由于`.crash`格式在近几年变化了。

首先，我们再看一下崩溃报告中的堆栈追踪：

>...
13 Crasher 0x000aeef6 0xa8000 + 28406 
...

最左边的十六进制值0x000aeef6是堆栈地址。第二个十六进制值0xa8000时应用加载的地址。前面带加号的数字28406是堆栈地址和加载地址相减的十进制值。你将会注意到崩溃报告下方的“Binary Images”是一个带有一些内存地址的动态库的列表。二进制的起始地址与堆栈追踪的加载地址是匹配的。

>Binary Images: 0xa8000 – 0xaffff Crasher armv7 /var/mobile/Containers/Bundle/Application/956755E3-6C66-4E87-A8BC-352FD4BE3711/Crasher.app/Crasher

接下来，为了好好测量，我们将会使用`file`或者`lipo -info`来验证我们的可执行文件包含我们崩溃的架构：

> file Crasher.app/Crasher

>Crasher.app/Crasher: Mach-O universal binary with 2 architectures Crasher.app/Crasher (for architecture armv7): Mach-O executable arm Crasher.app/Crasher (for architecture arm64): Mach-O 64-bit executable

现在我们已经拿到我们需要的所有东西。我们将会使用`atos`来将我们的地址转换成调试符号。注意看我们如何提供加载地址，紧跟着的是特定的崩溃的架构的堆栈地址：

> atos -arch armv7 -o Crasher.app/Crasher -l 0xa8000 0x000aeef6

>main (in Crasher) (main.m:14)

就是这样。如果你有兴趣深入钻研，可以阅读Mach-O对象文件格式并检查Mach-O的一系列命令行工具，也就是`otool`和`lipo`。

## 深入阅读

更全面的文档参见：

*   [Technical Note TN2151:
    Understanding and Analyzing iOS Application Crash Reports](https://developer.apple.com/library/ios/technotes/tn2151/_index.html#//apple_ref/doc/uid/DTS40008184)
*   [Technical Q&A QA1765: How to Match a Crash Report to a Build](https://developer.apple.com/library/ios/qa/qa1765/_index.html#//apple_ref/doc/uid/DTS40012196)
*   [Mach-O Programming Topics](https://developer.apple.com/library/mac/documentation/DeveloperTools/Conceptual/MachOTopics/0-Introduction/introduction.html)
*   [Objc.io on Mach-O Executables](http://www.objc.io/issue-6/mach-o-executables.html)