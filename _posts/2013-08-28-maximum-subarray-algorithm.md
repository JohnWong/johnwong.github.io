---
layout: post
title: "Maximum Subarray Algorithm"
category: past
description: 算法导论4.2-5提供了一种线性时间内解决的方法。
---
算法导论4.2-5提供了一种线性时间内解决的方法。

思路是，最大子串有一个特性，从前向后逐个累加，过程中和始终为正。这是因为如果计算到某个数，和为负，则去掉包括这个数的前面这部分，剩下的子串和会更大，这和之前认为的最大子串是冲突的。

因此从前往后逐个累加求和，如果和为负，则从下一个开始重新累加。在这个过程中找出和的最大值即可。


``` java
package cpt4;

import Utils.P;

public class Ex1s5 {

	/**
	 * find max subarray in O(n)
	 * @param array
	 * @return max < 0 means all are negative. max = 0 means all are zero.
	 */
	public static int[] maxSubarray(int[] d) {
		int max = Integer.MIN_VALUE;
		int start = 0, end = 0, tempStart = 0;
		int count = 0;
		for (int i = 0; i < d.length; i++) {
			count += d[i];
			if (count < 0) {
				count = 0;
				tempStart = i + 1;
			} else if (count > max) {
				max = count;
				start = tempStart;
				end = i;
			}
		}
		return new int[] { start, end, max };
	}

	public static void main(String[] args) {
		int[] d = { 13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15,
				-4, 7 };
		P.rintln(maxSubarray(d));
	}
}
```

早晨上班路上，想起来这个算法的正确性靠前面一条特性无法保证。查了下确实还需要另一个结论。[http://blog.csdn.net/joylnwang/article/details/6859677](http://blog.csdn.net/joylnwang/article/details/6859677)





