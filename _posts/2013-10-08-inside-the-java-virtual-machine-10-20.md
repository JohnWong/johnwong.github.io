---
layout: post
title: "深入Java虚拟机读书笔记[10:20]"
category: Past
description: Inside the Java Virtual Machine
---
### 第十章 栈和局部变量操作

### 第十一章 类型转换

### 第十二章 整数运算

### 第十三章 逻辑运算

### 第十四章 浮点运算

### 第十五章 对象和数组

### 第十六章 控制流

### 第十七章 异常

以上一些是操作码相关的内容，

### 第十八章 finally子句

#### 微型子例程
字节码中的finally子句表现的很像微型子例程。Java方法与微型子例程使用不同的指令集。跳转到微型子例程的指令是jsr或者jsr_w，将返回地址压入栈。执行完毕后调用ret指令。ret指令并不会从栈中弹出返回地址，而是在子例程开始的时候将返回地址从栈顶取出存储在局部变量，ret指令从局部变量中取出。这是因为finally子句本身会抛出异常或者含有return、break、continue等语句。finally确保会执行到，即使try或者catch中有return等语句。

### 第十九章 方法的调用与返回

实例方法和类方法区别：

a) 实例方法调用之前需要一个示例，类方法不需要  
b) 实例方法使用动态绑定，类方法使用静态绑定

调用的指令是invokevirtual和invokestatic。根据引用类型调用使用invokespecial，包括实例初始化、私有方法和super调用方法。在调用的引用类型是接口时使用invokeinterface。invokeinterface必须搜寻方法表而不是使用偏移量，因此速度比invokevirtual慢。

### 第二十章 指令invokespecial

### 第二十一章 线程同步

#### 监视器
Java中使用的同步机制是监视器，监视器支持两种线程：互斥和协作。通过对象锁实现互斥，允许多个线程在同一个共享数据上独立而互不干扰地工作。协作通过Object类的wait和notify方法，允许多个线程为同一个目标而共同工作。监视区域是最小的不可分割的代码块。在同一个监视器中，监视区域只会同时被一个线程执行。Java所使用的监视器被称为wait and notify监视器。Java虚拟机在执行wait命令时可以指定一个暂停时间。唤醒命令有两种：notify和notifyAll。notify命令随意从等待区中选择一个线程并标记为可能苏醒，notifyAll命令将等待区中的所有线程标记为可能苏醒。

#### 类锁用对象锁实现
锁住一个类实际上锁住的是类的Class对象。对于对象来说，Java虚拟机维护一个计数器，对象被加锁时计数加1。Java中有两种监视区域：同步语句和同步方法。每一个监视区域都和一个对象引用关联。同步语句块使用monitorenter和monitorexit两个操作码。对方法加锁比同步代码块更加高效。