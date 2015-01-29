---
layout: post
title: "2013亚马逊校招机试题B"
category: Past
description: 没通过还错过了有道面试。
---
题目参考[这里](http://discuss.leetcode.com/questions/223/jump-game-ii)，我觉得是个动态规划问题，写出的解法最终2/10个用例失败。做题太投入，看错了有道的面试时间，痛心疾首啊！

```java
static int walk(int[] array) {
	int[] t = new int[array.length];
	Arrays.fill(t, -1);
	t[0] = 0;
	for (int i = 0; i < array.length; i&#43;&#43;) {
		int d = array[i];
		if (d <= 0 || t[i] < 0)
			continue;
		for (int j = i &#43; 1; j <= i &#43; d && j < array.length; j&#43;&#43;) {
			t[j] = t[j] == -1 ? t[i] &#43; 1 : Math.min(t[j], t[i] &#43; 1);
		}
	}
	return t[array.length - 1] >= 0 ? t[array.length - 1]
			: -1;
}
```