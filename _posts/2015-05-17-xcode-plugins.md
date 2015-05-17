---
layout: post
title: 使用Xcode插件加速开发
category: Mobile
description: 入行iOS以来对Xcode插件的总结。
thumb: /images/2015-05-17-xcode-plugins.png
---

相信大多数iOS开发者都会使用Xcode来加速开发。我把我在这方面积累的知识记录下来。

## 使用Alcatraz安装插件

传统的Xcode插件的安装是拉代码下来，打开工程并运行，将编译的插件包拷贝到指定目录下。这种方式比较麻烦，并且没有一个地方可以挑选有用的插件。
[Alcatraz]是一个非常好用的Xcode插件管理工具。有了这个工具，插件安装和卸载只需要点点鼠标，还可以搜索、浏览各种插件。

需要安装命令行工具，如果没有安装可以通过`Preferences > Downloads`来安装。安装[Alcatraz]方法非常简单：

```
curl -fsSL https://raw.github.com/supermarin/Alcatraz/master/Scripts/install.sh | sh
```

使用方法非常简单，通过`Window > Package Manager`来打开下图窗口。在窗口内可以浏览或者搜索插件、主题或者模版。每个插件都会有一张动图来演示插件的使用效果。点击前面的`Install`或者`Remove`就可以安装或者卸载。

![Install](https://camo.githubusercontent.com/919efe4e1e53237df51d7010c862bd5c04fd6a70/687474703a2f2f616c63617472617a2e696f2f696d616765732f73637265656e73686f744032782e706e67)

## 插件推荐

以下是我常用或者觉得有用的插件。读者还可以参考其他Xcode插件推荐文章，比如NSHipster的文章[Xcode Plugins](http://nshipster.com/xcode-plugins/)，[那些不能错过的Xcode插件](http://www.cocoachina.com/industry/20130918/7022.html)。

#### Auto-Importer

这个插件可以帮助你快速import头文件。编写代码的过程中，写下一个类，不需要跳到文件头部添加import语句，只需要command+ctrl+H就可以搞定。

#### BBUFullIssueNavigator

Xcode的issue navigator通常对issue的内容只会显示2行，点击后才能看到全部内容。这个插件可以在issue navigator中直接显示issue全部内容。

#### CocoaPods

每次更新CocoaPods时不必命令行打开项目，敲入命令。只需要点击`Product > CocoaPods > Install Pods`。另外还提供了创建Podfile和Podspec的功能。

#### DerivedData Exterminator

使用Xcode时会遇到一些编译的坑，光靠clean远远不够。有时清理derived data可以解决，有时需要清理module cache。使用这个插件，可以在Xcode的`View`菜单下找到这些功能。还可以在工具栏显示按钮，清理derived data更方便。

#### KSImageNamed

代码中需要使用图片的时候，通常是在输入代码imageNamed后。安装这个插件后，就会在此时给出自动完成选项，列出项目内所有图片。还可以同时预览选中的图片。

#### OpenInTerminal

有时候我们需要在命令行中对项目做一些事情，那么需要打开命令行，切换目录。安装这个插件后可以通过`Navigator > Reveal in Terminal`或者`command + alt + T`来完成。

#### VVDocument

喵神写的Xcode插件。通过敲击三次`/`就可以生成规范的注释。

#### ZLGotoSandbox

有时候我们检查查看模拟器的应用安装目录。这个插件可以通过`File > Go to Sandbox!`来打开模拟器内应用的目录。

#### OMColorSense

可以在编写代码创建UIColor/NSColor时预览最终的颜色。因为很少直接使用UIColor提供的方法来创建颜色，所以这个插件用得并不多。另外，如果你觉得UIColor创建RGB比较繁琐，可以试试[HEXCOLOR](https://gist.github.com/JohnWong/6dcc561c6e8228e99f8b)，代码来自手淘。

#### Helmet

开发过程中经常需要查看iOS SDK的头文件。如果不小心修改了，就会编译出错，需要删除module cache后清理工程。装了Helmet就可以阻止对SDK头文件的误修改。这个问题我是通过另一种方法给这些framework加锁，已经记不清怎么做的了。

#### HOStringSense

在Xcode中代码加入字符串时，需要自行做符号转义，字符数计算。HOStringSense可以帮助你完成这些任务。

#### XVim

据说时Vim党的福音，可以像操作Vim一样操作Xcode编辑器。试用了一段时间导致Xcode崩溃过，学习了一段时间的Vim快捷键，始终觉得不如触摸板方便，放弃了。

#### XcodeBoost

选中变量的时候，把这个变量出现的所有地方都高亮显示。对于修改变量检查代码来说非常方便。最初看到类似的功能是在Sublime Text上，觉得真好用。

#### SCXcodeMiniMap

编辑源代码时，展示代码的迷你地图。源代码比较多时，可以通过迷你地图来找到想要查看的代码位置，点击就可以跳转过去。这个功能最初也是在Sublime Text上看到的，非常方便。

## 插件升级

每次Xcode升级的时候都会出现插件消失的情况。这是由于插件开发时，需要声明兼容的Xcode的UUID列表。升级Xcode后需要插件作者更新插件支持新的Xcode，开发这升级Xcode。如果开发者没及时更新就暂时不能用了。[Stack Overflow](http://stackoverflow.com/questions/22324303/the-plugin-didnt-work-on-xcode-5-1)上有一个简单的办法，将新Xcode的UUID写入已经安装的Xcode插件的兼容列表。手动一个一个地修改太过繁琐，同事写了一段脚本来实现这个功能[Xcode Plugin Auto Compatible.sh](https://gist.github.com/sodabiscuit/41196f0ceb80bb9fdcd5)。大多数情况下这么做就可以让插件在新的Xcode下可以使用。有些情况下有可能出现某个插件在引起Xcode崩溃。这时就比较麻烦了，需要尝试一个一个地禁用插件来找到出问题的那个，卸载掉。

[Alcatraz]:https://github.com/supermarin/Alcatraz