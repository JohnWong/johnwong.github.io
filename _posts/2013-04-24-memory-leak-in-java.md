---
layout: post
title:  Java内存泄露
category: past
description: Java内存泄漏与C++原理不同。
---

#### 1. Java内存泄漏与C++的区别

在Java 中，内存泄漏就是存在一些被分配的对象，这些对象有下面两个特点，首先，这些对象是可达的，即在有向图中，存在通路可以与其相连；其次，这些对象是无用的，即程序以后不会再使用这些对象。如果对象满足这两个条件，这些对象就可以判定为Java 中的内存泄漏，这些对象不会被GC 所回收，然而它却占用内存。在C++中，内存泄漏的范围更大一些。有些对象被分配了内存空间，然后却不可达，由于C++中没有GC，这些内存将永远收不回来。在Java 中，这些不可达的对象都由GC 负责回收，因此程序员不需要考虑这部分的内存泄漏。

#### 2. 内存泄露示例

```java
Vector v = new Vector(10);  
for (int i = 1; i < 100; i++) {  
    Object o = new Object();  
    v.add(o);  
    o = null;  
}
```

Vector中引用的对象存在引用未被释放，出现内存泄漏。

#### 3. 内存泄漏原因

3.1 静态集合类如HashMap，Vector。

3.2 监听器，例如addXXXListener()释放的时候需要删除监听器

3.3 物理连接，如数据库连接，网络连接，不使用的时候需要close。如果使用连接池，显式关闭连接外还需要显式关闭ResultSet Statement对象。

附：subString的内存泄漏

```java
List<String> handler = new ArrayList<String>();  
for (int i = 0; i < 1000; i++) {  
    String str = new String(new char[10000000]);  
    handler.add(str.substring(1, 5));  
}
```

分析subString源码：

```java
String(int offset, int count, char value[]) {  
    this.value = value;  
    this.offset = offset;  
    this.count = count;  
}
```

实际上为了加快运行的效率，牺牲了内存空间。导致subString得到的对象占用空间并未减少。因此需要调用其拷贝构造方法，修改为

```java
handler.add(new String(str.substring(1, 5))); 
```

分析该构造方法的代码，如果String的大小比其中包含的char数组大小要小，那么就做一次部分拷贝。否则与subString方法类似。