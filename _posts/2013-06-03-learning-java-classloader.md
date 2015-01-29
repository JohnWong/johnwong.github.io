---
layout: post
title: "Java ClassLoader详解"
category: Past
description: 深入Java虚拟机，ClassLoader是其中重要的一个环节。
---
深入Java虚拟机，ClassLoader是其中重要的一个环节。看书&#43;查资料&#43;动手，整理出如下要点：

1. Class loader using following four steps:
a, Bootstrap ClassLoader/启动类加载器
主要负责jdk_home/lib目录下的核心 api 或 -Xbootclasspath 选项指定的jar包装入工作.
b, Extension ClassLoader/扩展类加载器
主要负责jdk_home/lib/ext目录下的jar包或 -Djava.ext.dirs 指定目录下的jar包装入工作
c, System ClassLoader/系统类加载器
主要负责java -classpath/-Djava.class.path所指的目录下的类与jar包装入工作.
b, User Custom ClassLoader/用户自定义类加载器(java.lang.ClassLoader的子类)在程序运行期间, 通过java.lang.ClassLoader的子类动态加载class文件, 体现java动态实时类装入特性.
加载顺序是：自底向上检查类是否已经装在，有则返回，否则自顶向下尝试加载类。

![2013-06-03-learning-java-classloader](/images/2013-06-03-learning-java-classloader.png)

2. 类装入的方式有两种 —— 显式 或 隐式，两者之间有些细微差异。显式 类装入发生在使用以下方法调用装入的类的时候：
cl.loadClass()（cl 是 java.lang.ClassLoader 的实例）
Class.forName()（启动的类装入器是当前类定义的类装入器）
隐式 类装入发生在由于引用、实例化或继承导致装入类的时候（不是通过显式方法调用）。在每种情况下，装入都是在幕后启动的，JVM 会解析必要的引用并装入类。与显式类装入一样，如果类已经装入了，那么只是返回一个引用；否则，装入器会通过委托模型装入类。
3. 项目源码与jar中存在同包名同类名的类，运行时加载源码中该类原因：他们都属于User classes，由系统类加载器加载。加载的时候搜索路径顺序：
a. 缺省值：调用java或javaw的当前路径，是项目class所在目录
b. 环境变量classpath设置的路径
c. 执行Java命令行-classpath或-cp的值。如果指定了这两个命令行参数之一,它的值会覆盖环境变量CLASSPATH的值。
d. -jar 选项:如果通过java -jar 来运行一个可执行的jar包,这当前jar包会覆盖上面所有的值.换句话说,-jar 后面所跟的jar包的优先级别最高,如果指定了-jar选项,所有环境变量和命令行制定的搜索路径都将被忽略.JVM APPClassloader将只会以jar包为搜索范围. 有关可执行jar有许多相关的安全方面的描述,可以参考http://java.sun.com/docs/books/tutorial/jar/ 来全面了解. 这也是为什么应用程序打包成可执行的jar包后,不管你怎么设置classpath都不能引用到第三方jar包的东西了.

另附ClassLoader.loadClass与Class.forName的区别，主要在于是否初始化：

```java
public class Test {

	public static void main(String[] argv) throws ClassNotFoundException,
			InstantiationException, IllegalAccessException {
//		Class classT = ClassLoader.getSystemClassLoader().loadClass("Ti"); //not print static
//		Class classT = Class.forName("Ti"); //print static
//		Class classT = Class.forName("Ti", true, ClassLoader.getSystemClassLoader()); //print static
		Class classT = Class.forName("Ti", false, ClassLoader.getSystemClassLoader()); // not print static
	}
}

class Ti {
	static {
		System.out.println("static");
	}
}
```




