---
layout: post
title: FauxPas试用时间破解
category: Mobile
description: 抽空试着hack一下FauxPas。
thumb: images/2015-06-02-hack-fauxpas.jpg
---

以下内容仅用于学习逆向工程。用到的工具有Hopper，lldb。

FauxPas是一款非常不错的项目检查工具。之前写过[用FauxPas找到潜在Bug](http://johnwong.github.io/mobile/2014/08/29/using-fauxpas.html)，介绍了FauxPas的功能。在使用过期后，尝试hack一下。

### 绕过证书窗口

使用的是1.4版本的FauxPas，先拖入Hopper，找到方法`-[XAAppDelegate applicationDidFinishLaunching:]`。读汇编代码到`00000001000043cc`时，可以看到一个条件跳转，后面的方法有 `@selector(enterLockdownMode)` 和 `@selector(trialNagVC)` 。那么看起来这里如果不跳转会跳出试用失败窗口，我们修改成

```
00000001000043cc jmp 0x10000446b
```

这时候运行起来，打开了程序的主窗口，但是无法使用，菜单栏的打开是禁用的。

### 解锁UI

这个问题解决起来花费的时间比较多。将AppDelegate里的调用去掉了，UI依然未解锁。最后想到了直接去搞getter方法。找到了方法`-[XAAppDelegate userInterfaceEnabled]:`，这个方法里唯一的跳转，通过lldb调试发现走到了跳走的分支。我们把跳转禁用，UI就可以使用了。

```
0000000100004e56 nop
```

### 阻止Sparkle弹窗

现在可以使用了，但是每次打开应用都会提示`Insecure update error!`。可以从弹窗中读到使用了[Sparkle](https://github.com/sparkle-project/Sparkle)来做程序升级。在Github上的项目里搜索这段错误代码，找到所在的类`SUUpdater`。在代码里找到调用的地方

```
0000000100004cbd         mov        rdi, qword [ds:objc_cls_ref_SUUpdater]
```

lldb调试也证实这里会在启动时被调用，随后弹窗。然后让后面调用的逻辑失效。

```
0000000100004ccb nop
```

### 解除试用倒计时

至此基本完成了，唯一的遗憾是打开项目开始检查时会有15秒的倒计时，暂时还没有找到hack的方法。

