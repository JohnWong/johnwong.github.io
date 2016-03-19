---
layout: post
title: "阿里巴巴2014校招笔试错误汇总"
category: past
description: 还好通过了。。。
---
试题参见：`http://7-sun.com/text/9484.html`（已失效）

1\. C 觉得内存和SSD都使用闪存芯片，速度应该接近。实际上还受限于接口等，内存纳秒级时间可以访问。

7\. A 判断有向图是否存在回路的最佳方法是拓扑排序。

22\. ABC 进程与作业不是一一对应的

23\. BD

错误最严重的就是Java选做题了。

```java
import static java.lang.Math.*;
import static java.util.Arrays.*;
import java.io.*;
import java.util.*;

public class Test {

	static Test test1 = new Test("t1");
	static Test test2 = new Test("t2");
	static int i = print("i");
	static int n = 99;
	{
		System.out.println("构造块");
	}
	static {
		System.out.println("静态块");
	}
	static int print(String tag){
		System.out.println(tag &#43; " i=" &#43; i &#43; " n="&#43;n);
		&#43;&#43;n;
		return &#43;&#43;i;
	}
	public Test(String tag){
		i=print(tag);
	}
	
	public static void main(String[] args) {
		Test t = new Test("init");
	}
}
```

运行的结果是：

```
构造块
t1 i=0 n=0
构造块
t2 i=1 n=1
i i=2 n=2
静态块
构造块
init i=3 n=99
```