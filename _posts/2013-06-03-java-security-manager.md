---
layout: post
title: "Java SecurityManager"
category: Past
description: Java的SecurityManager用于完成对一些本地方法的权限管理。
---
Java的SecurityManager用于完成对一些本地方法的权限管理。其他安全特性可以保证程序Java程序安全运行，但是当调用本地方法时，Java安全沙箱完全不起作用，因此需要在调用本地方法前确认它是可信任的。

启动SecurityManager开关：

默认情况下，JVM是不启动安全检查的。打开的方式有两种：一种是在启动运行中追加JVM参数-Djava.security.manager，另一种方式是在程序中直接设置：System.setSecurityManager(new SecurityManager())。第二种方法可以设置为系统的SecurityManager或者自定义类扩展该类。这两种方式是等价的，但是不能同时使用。

Java安全管理器控制权限的方法：

使用系统的SecurityManager 编写.policy文件；扩展SecurityManager修改其check方法，使用上述第二种方法启动SecurityManager。使用系统的SecurityManager需要修改policy文件：修改jvm自带的java.policy文件，或者指定为另一个文件。java.policy文件位于%JAVA_HOME%/ jre/lib/security/。指定为其他方法启动时加参数-Djava.security.policy=c:/all.policy。另外在调试过程中我使用了命令行的方式编译带包声明的Java，与不带包声明的方式有点差别，命令如下：

```
set classpath=.
javac -d ./ Test.java  #第二个参数
java monitor.Test
```

SecurityManager中做权限检查实际上调用的是AccessController来完成检查。检查的过程是从栈顶开始，一直检查到栈底部，遇到某个类的保护域没有权限则抛出异常。这样的算法防止了任何代码执行任何不信任的代码。有的时候靠近栈顶的代码希望之星一段代码，而这段代码在较下层不允许执行，例如一个不可靠的applet请求Java API加载字体，因此需要打开这个字体文件的权限。这种情况下AccessController的doPrivileged方法可以解决问题。检查权限的过程中，检查到doPrivileged方法后，检查到调用其的类后不再继续检查。