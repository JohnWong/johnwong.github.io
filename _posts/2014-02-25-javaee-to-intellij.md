---
layout: post
title: "JavaEE项目切换到Intellij遇到的一个问题"
category: past
description: 买了MBP开心换电脑。
---
换电脑真是一个麻烦的事情，尤其是像我这样需要各种环境的人。第一天折腾xcode，弄好证书什么的，把之前的一个项目跑起来。今天是折腾的第二天，只完成了一件事情，就是在mac上用Intellij Idea把之前一个项目跑起来。真心受不了MyEclipse了，慢就算了，把项目导入遇到问题，结果啥也没导入进来，根本不给修改配置解决问题的机会。

问题是这样的，用Intellij新建项目，把之前的代码资源拷贝过来，运行没有问题。修改了一点代码，部署的时候代码始终没有更新。项目输出目录下，production下是更新了的，artifacts下是没更新的。重新编译、换web容器都没有用。最后发现是拷贝过来的WEB-INF目录中已经编译好的classes的问题。Eclipse是将编译好的class文件放在这个目录，Intellij编译好的并不放在这里，不知道哪一步就导致这里的classes文件复制到输出目录，并导致新编译的class文件被覆盖。

解决方法就是把web目录下的classes目录删除掉。

