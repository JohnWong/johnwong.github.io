---
layout: post
title: Reveal App试用时间破解
category: Mobile
description: 抽空试着hack一下应用调试利器Reveal。
thumb: /images/2015-05-20-hack-reveal-app.png
---

以下内容仅用于学习逆向工程。用到的工具有Hopper，lldb。

iOS应用调试利器Reveal不必多介绍。应用可以免费试用。目测时间校验并不严谨，修改系统时间就可以将试用状态从已过期变为未过期。先改时间到多天以后，运行会弹出“Your free trial of Reveal has expired”。接下来切入正题。

### 寻找关键代码

使用的是1.5.1的Reveal，先拖入Hopper。根据提示我们猜测使用过期的一些代码可能与“trial”有关，在左侧的搜索框搜索这个词。

![img1](//dn-johnwong.qbox.me/images/2015-05-20-hack-reveal-app-01.png)

许多结果都是`IBATrialModeReminderWindowController`来自这个类，看起来是试用的提示窗。可以看到初始化方法`[IBATrialModeReminderWindowController controller]`及其地址`0000000100077940`。尝试用GDB调试，打开命令行，切换到目录`/Applications/Reveal.app/Contents/MacOS`，然后使用GDB调试。

```
gdb Reveal
(gdb) b *0x0000000100077940
(gdb) r
(gdb) bt
```

结果看到调用堆栈如下：

```
#0  0x0000000100077940 in std::__1::shared_ptr<IBATrialDateStorageInterface>::shared_ptr<IBANSUserDefaultsTrialDateStorage, void>(IBANSUserDefaultsTrialDateStorage*) ()
#1  0x0000000100079779 in std::__1::shared_ptr<IBATrialDateStorageInterface>::shared_ptr<IBANSUserDefaultsTrialDateStorage, void>(IBANSUserDefaultsTrialDateStorage*) ()
#2  0x000000010007992a in std::__1::shared_ptr<IBATrialDateStorageInterface>::shared_ptr<IBANSUserDefaultsTrialDateStorage, void>(IBANSUserDefaultsTrialDateStorage*) ()
#3  0x000000010001f534 in _mh_execute_header ()
```

调用堆栈感觉不太对劲，放弃。

### 绕过过期弹窗

之前搜索结果还有一些来自`IBATrialModeReminderPresenter`这个类。`-[IBATrialModeReminderPresenter shouldShowTrialModeSheet]`方法看起来判断是否显示试用窗口。`0000000100079678`处有跳转的汇编指令，我们尝试改改它。选中这一行，选择菜单栏的`Modify > Assemble Instruction...`，将jne修改成je，然后点击`Assemble and Go Next`。

![img1](//dn-johnwong.qbox.me/images/2015-05-20-hack-reveal-app-02.png)

然后生成新的可执行文件。备份`/Applications/Reveal.app/Contents/MacOS/Reveal`。点击`File > Produce New Executable...`，并替换为新的可执行文件。运行会提示`This copy of Reveal is damaged`。

### 绕过应用自身校验

浏览一堆方法，看到了`[IBAAppDelegate verifyCodeSignature]`这个方法，用来在应用启动时做签名校验。部分汇编代码如下。

```
000000010008f3de         je         0x10008f3e9

000000010008f3e0         test       r15b, r15b
000000010008f3e3         jne        0x10008f662

000000010008f3e9         mov        rax, qword [ds:objc_cls_ref_NSAlert]
000000010008f3f0         mov        qword [ss:rbp-0x70+var_48], rax
000000010008f3f4         mov        rdi, qword [ds:objc_cls_ref_NSBundle]
000000010008f3fb         mov        rsi, qword [ds:0x1001dda18]
000000010008f402         mov        rbx, qword [ds:imp___got__objc_msgSend]
000000010008f409         call       rbx
000000010008f40b         mov        rdi, rax
000000010008f40e         call       imp___stubs__objc_retainAutoreleasedReturnValue
000000010008f413         mov        qword [ss:rbp-0x70+var_56], rax
000000010008f417         mov        rsi, qword [ds:0x1001ddca8]
000000010008f41e         lea        rdx, qword [ds:cfstring_This_copy_of_Reveal_is_damaged] ; @"This copy of Reveal is damaged"
```

方法内的第一个je跳转到`0x10008f3e9`。从这个地址往下看，能够看到"This copy of Reveal is damaged"，说明这个跳转会提示签名问题。我们尝试将这里的je替换为jne，应用崩溃了。将je替换为`jmp 0x10008f662`，再次运行Reveal。弹出框提示“Insecure update error!”。点击确定，Reveal可以运行起来，绕过了试用限制的弹窗。

### 屏蔽升级功能

每次打开都会弹窗都会提示这个，还是不爽。试着用签名的方法解决，遇到问题签名失败。读这个提示框的内容，看到了Sparkle，应该是个应用升级组件。那么把升级功能去掉应该就不会弹窗了。搜索`Sparkle`，找到一个方法`-[IBAAppDelegate configureSparkle]`。我们能够看到方法内先判断是否Sparkle是否enable，然后做Sparkle的初始化。我们只需要把跳转语句je改为jne，那么升级功能就会去掉，也就不会弹出那个框。试了一下果真如此。至此过程全部结束。

![img1](//dn-johnwong.qbox.me/images/2015-05-20-hack-reveal-app-03.png)

### 去掉标题栏过期提示

窗口右上角的过期提示有点惹眼，去掉。

```
000000010007be25 nop
```
