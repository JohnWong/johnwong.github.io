---
layout: post
title: "深入Java虚拟机读书笔记[1:4]"
category: past
description: Inside the Java Virtual Machine
---
### 第一章 Java体系结构

#### 1\. Java体系结构

* the Java programming language 
* the Java class file format 
* the Java Application Programming Interface 
* the Java Virtual Machine

#### 2\. Java语言优点或使用的技术：

* object-orientation 
* multi-threading 
* structured error-handling 
* garbage collection 
* dynamic linking 
* dynamic extension

#### 3\. 平台无关性，安全性和网络移动性使得java与发展中的网络计算环境相得益彰
 
### 第三章 安全
 
#### 1\. 组成Java沙箱的基本组件：

* the class loader architecture 
* the class file verifier 
* safety features built into the Java Virtual Machine (and the language) 
* the security manager and the Java API

#### 2\. Class loader using following four steps:

a, Bootstrap ClassLoader/启动类加载器

主要负责jdk_home/lib目录下的核心 api 或 -Xbootclasspath 选项指定的jar包装入工作.

b, Extension ClassLoader/扩展类加载器

主要负责jdk_home/lib/ext目录下的jar包或 -Djava.ext.dirs 指定目录下的jar包装入工作

c, System ClassLoader/系统类加载器

主要负责java -classpath/-Djava.class.path所指的目录下的类与jar包装入工作.

b, User Custom ClassLoader/用户自定义类加载器(java.lang.ClassLoader的子类)

在程序运行期间, 通过java.lang.ClassLoader的子类动态加载class文件, 体现java动态实时类装入特性.

#### 3\. 类装入的方式有两种 —— 显式 或 隐式，两者之间有些细微差异。显式 类装入发生在使用以下方法调用装入的类的时候：

cl.loadClass()（cl 是 java.lang.ClassLoader 的实例）
Class.forName()（启动的类装入器是当前类定义的类装入器）
隐式 类装入发生在由于引用、实例化或继承导致装入类的时候（不是通过显式方法调用）。在每种情况下，装入都是在幕后启动的，JVM 会解析必要的引用并装入类。与显式类装入一样，如果类已经装入了，那么只是返回一个引用；否则，装入器会通过委托模型装入类。

#### 4\. 项目源码与jar中存在同包名同类名的类，运行时加载源码中该类原因：他们都属于User classes，由系统类加载器加载。加载的时候搜索路径顺序：

a. 缺省值：调用java或javaw的当前路径，是项目class所在目录
b. 环境变量classpath设置的路径
c. 执行Java命令行-classpath或-cp的值。如果指定了这两个命令行参数之一,它的值会覆盖环境变量CLASSPATH的值。
d. -jar 选项:如果通过java -jar 来运行一个可执行的jar包,这当前jar包会覆盖上面所有的值.换句话说,-jar 后面所跟的jar包的优先级别最高,如果指定了-jar选项,所有环境变量和命令行制定的搜索路径都将被忽略.JVM APPClassloader将只会以jar包为搜索范围. 有关可执行jar有许多相关的安全方面的描述,可以参考http://java.sun.com/docs/books/tutorial/jar/ 来全面了解. 这也是为什么应用程序打包成可执行的jar包后,不管你怎么设置classpath都不能引用到第三方jar包的东西了.

#### 5\. Class file verifier

a. Basic format check(When class is loaded)  
b. Additional verification(When linking)  
c. Bytecode verification(When linking)  
d. Virtual pass(Code invoked)

#### 6\. Safety features built into the Java Virtual Machine

* type-safe reference casting 
* structured memory access (no pointer arithmetic)
* automatic garbage collection (canít explicitly free allocated memory)
* array bounds checking 
* checking references for null

#### 7\. The security manager and the Java API

#### 8\. Code sign and authentication

#### 9\. AccessController与保护域

### 第四章

#### 1\. A New Software Paradigm

软件开始呈现一种容器的特性，用户不必担心安装升级软件版本的问题。因为代码和数据一起通过网络传输，所以软件可以自动发布和升级。

#### 2\. 对网络移动性的支持

a) 平台无关性与安全性  
b) 动态连接（用到时才加载类）  
c) 动态扩展（loadClass或者forName可以使运行中的程序去调用在源代码中未曾提及的，而是在程序运行中决定的类型）  
e) 紧凑的class文件  
f) 非体系结构必须的策略（jar格式减少传输时间、不按需下载减少等待时间）
