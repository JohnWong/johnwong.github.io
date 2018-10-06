---
layout: post
title: 用Git的方式使用SVN
category: mobile
description: 必须用SVN但还是喜欢Git，还好有git-svn
thumb: /images/2015-04-30-using-git-with-svn.png
---

习惯用Git后的程序员一定对SVN不屑一顾。不过目前的开发环境必须使用SVN，用起来不开心。还好Git提供了对SVN的支持，让我们可以像使用Git一样使用SVN。当然一些Git的高级功能还是无法支持的。

有兴趣详细了解的同学可以参考[git-svn文档](http://git-scm.com/docs/git-svn)。简单来说只需要几步就可以使用了。

#### 检出SVN库

git svn clone http://PATH_TO_SVN

有了这一步就可以在命令行像操作Git一样操作SVN了。如果对git-svn的命令不习惯，可以试试用工具。

#### 使用SourceTree

我经常使用的Git客户端是SourceTree。SourceTree支持git-svn，只需要将检出的目录拖到SourceTree的Repository Browser (Command + B)，就可以使用了。

如果使用时遇到错误：

```
Can’t locate SVN/Core.pm in @INC (you may need to install the SVN::Core module)
```

解决方法是参考[这里](http://blog.puhao.me/%E5%90%90%E6%A7%BD/OS-X-Yosemite(10.10)%E4%B8%8B%E6%97%A0%E6%B3%95%E4%BD%BF%E7%94%A8git-svn%E8%A7%A3%E5%86%B3%E6%96%B9%E6%B3%95/)：

```
sudo ln -s /Applications/Xcode.app/Contents/Developer/Library/Perl/5.18/darwin-thread-multi-2level/SVN /System/Library/Perl/Extras/5.18/SVN
sudo ln -s /Applications/Xcode.app/Contents/Developer/Library/Perl/5.18/darwin-thread-multi-2level/auto/SVN/ /System/Library/Perl/Extras/5.18/auto/SVN
```

然后就可以开心地继续开发了。

![git-svn](/images/2015-04-30-using-git-with-svn.png)

#### 自定义Action

使用过程中，因为我有一些改动不需要提交到svn上，所以每次提交或者更新时都需要先stash，完成操作再放回来。这样3步操作可以通过Source Tree的自定义Action合成一步。

定义了一些脚本`pull.sh`和`push.sh`，例如：

```PowerShell
#!/bin/sh
cd "$REPO"
git stash
git svn fetch
git svn rebase
git stash apply
```

```PowerShell
#!/bin/sh
cd "$REPO"
git stash
git svn dcommit
git stash apply
```

打开Source Tree的`Preferences->Custom Actions`，新建pull与push，选择这两个脚本。以后打开项目后，就可以在`Actions->Custom Actions`下找到你添加的这两个Action。