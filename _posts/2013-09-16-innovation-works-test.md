---
layout: post
title: "创新工场的一道笔试题"
category: past
description: 创新工场笔试打酱油了。
---
整个卷子出错的问题是堆排序，堆调整有一个参数写错了。几周不看，就出错了，看来考前一定要温习。

不会的题是写手动开平方。

```java
static double sqrt(int a, int k) {
	double x = 1.0;
	double d = (k - 1.0) / k;
	double ox = 0;
	while (Math.abs(ox - x) > 0.0000001) {
		ox = x;
		x = d * x &#43; a / (k * Math.pow(x, k - 1));
		System.out.println(Math.abs(ox - x));
	}
	return x;
}
```

[http://www.guokr.com/question/461510/](http://www.guokr.com/question/461510/)

吐槽一下，那个DeNA的笔试感觉很简单啊，除了一道填空外多应该没问题，结果挂了。。。