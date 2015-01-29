---
layout: post
title: "Code Jam 2010 Round 1A Problem B"
category: Past
description: Code Jam练习
---
### Problem B. Make it Smooth

#### Problem

You have a one-dimensional array of N pixels. Each pixel has a value, represented by a number between 0 and 255, inclusive. The distance between two pixels is the absolute difference of their numbers.
You can perform each of the following operations zero or more times:
With cost D, delete any pixel, so its original neighbors become neighboring pixels.
With cost I, insert one pixel of any value into any position -- either between two existing pixels, or before the first pixel, or after the last pixel.
You can change the value of any pixel. The cost is the absolute difference of the old value of the pixel and the new value of the pixel.
The array is smooth if any neighboring pixels have distance at most M. Find the minimum possible cost of a sequence of operations that makes the array smooth.

Note: The empty array -- the array containing no pixels -- is considered to be smooth.

#### Input

The first line of the input gives the number of test cases, T. T test cases follow, each with two lines. The first line is in the form "D I M N", the next line contains N numbers ai: the values of the pixels from left to the right.

#### Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1), and y is the minimum cost to make the input array smooth.

#### Limits

All the numbers in the input are integers.
1 ≤ T ≤ 100
0 ≤ D, I, M, ai ≤ 255
Small dataset
1 ≤ N ≤ 3.

#### Large dataset

1 ≤ N ≤ 100.

#### Sample

```
Input 
 
2
6 6 2 3
1 7 5
100 1 5 3
1 50 7
 	
Output 

Case #1: 4
Case #2: 17
```

#### Explanation

In Case #1, decreasing the 7 to 3 costs 4 and is the cheapest solution. In Case #2, deleting is extremely expensive; it's cheaper to insert elements so your final array looks like [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 50, 45, 40, 35, 30, 25, 20, 15, 10, 7].

解题思路：

最近遇到的一些动态规划问题中感觉最难的一个，思考明白后让我对动态规划的理解更深刻了。思路是这个数组中的每个数字在最小代价时，不确定大小，但是在0-255范围内把每种不同组合的情况都考虑到，找出其中最小的代价。在找的过程中，可以先找数组前1个的最小代价，然后利用前1个的结论找前2个的最小代价，也就是用动态规划的思想递归求解。在定义数组a[N]，存放输入的N个记录。定义dp[N+1][256]，例如dp[i+1][j]的意义是，a的子数组a[0:i]中最后一个像素变为j时的最小代价。可能的情况有：

1. 删除a[i+1]，那么cost=dp[i][j] + D，即a[i]变为j的代价加上删除a[i+1]代价。 

2. 修改a[i+1]变为j，那么需要考虑a[i]不同情况，我们使用辅助变量k表示a[i]的不同情况，0<=k<=255。cost=dp[i][k]+insert_cost+move_cost，其中move_cost指的是将a[i+1]修改为j的代价，insert_cost指的是将k到j之间通过插入使之平滑的代价。

求出删除a[i+1]与k取不同值时修改a[i+1]的代价的最小值，即为a[i+1][j]的值。接下来只需要找出dp[N][0:255]中的最小值，即为答案。

```java
void run() {
	int C = sc.nextInt();
	double ratio = (1 + sqrt(5)) / 2;
	for (int c = 1; c <= C; c++) {
		int a1 = sc.nextInt();
		int a2 = sc.nextInt();
		int b1 = sc.nextInt();
		int b2 = sc.nextInt();
		long count = 0;
		for (int i = a1; i <= a2; i++) {
			double up = i * ratio;
			double down = i / ratio;
			if (b1 >= up || b2 <= down)
				count += b2 - b1 + 1;
			else {
				if (b1 <= down)
					count += max(0, (int) floor(down) - b1 + 1);
				if (b2 >= up)
					count += max(0, b2 - (int) ceil(up) + 1);
			}
		}
		System.out.println(String.format("Case #%d: %d", c, count));
	}
}
```






