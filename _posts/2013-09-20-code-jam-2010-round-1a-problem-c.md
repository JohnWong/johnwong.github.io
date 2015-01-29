---
layout: post
title: "Code Jam 2010 Round 1A Problem C"
category: Past
description: Code Jam练习
---
### Problem C. Number Game

#### Problem

Arya and Bran are playing a game. Initially, two positive integers A and B are written on a blackboard. The players take turns, starting with Arya. On his or her turn, a player can replace A with A - k*B for any positive integer k, or replace B with B - k*A for any positive integer k. The first person to make one of the numbers drop to zero or below loses.

For example, if the numbers are initially (12, 51), the game might progress as follows:

Arya replaces 51 with 51 - 3*12 = 15, leaving (12, 15) on the blackboard.
Bran replaces 15 with 15 - 1*12 = 3, leaving (12, 3) on the blackboard.
Arya replaces 12 with 12 - 3*3 = 3, leaving (3, 3) on the blackboard.
Bran replaces one 3 with 3 - 1*3 = 0, and loses.
We will say (A, B) is a winning position if Arya can always win a game that starts with (A,B) on the blackboard, no matter what Bran does.
Given four integers A1, A2, B1, B2, count how many winning positions (A, B) there are with A1 ≤ A ≤ A2 and B1 ≤ B ≤ B2.

#### Input
The first line of the input gives the number of test cases, T. T test cases follow, one per line. Each line contains the four integers A1, A2, B1, B2, separated by spaces.

#### Output
For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1), and y is the number of winning positions (A, B) with A1 ≤ A ≤ A2 and B1≤ B ≤ B2.

#### Limits
1 ≤ T ≤ 100. 
1 ≤ A1 ≤ A2 ≤ 1,000,000.
1 ≤ B1 ≤ B2 ≤ 1,000,000.

#### Small dataset
A2 - A1 ≤ 30.
B2 - B1 ≤ 30.

#### Large dataset
A2 - A1 ≤ 999,999.
B2 - B1 ≤ 999,999.

No additional constraints.

#### Sample

```
Input  
 
3
5 5 8 8
11 11 2 2
1 6 1 6
 	
Output

Case #1: 0
Case #2: 1
Case #3: 20
```

解题思路：终于把动态规划理解的差不多了，用动态规划写了解法，做了一些优化，可以解决小数据量。但是大数据量效率太差等不到解出来的时刻了。看了解析才知道这是又玩起组合游戏。高效解决问题基于2点：
1. If A ≥ 2B, then (A, B) is a winning position.
设k使得0<A-kB<B，那么(A-kB, B)如果必败，那么我们就减去kB。如果(A-kB, B)必胜，那么我们见减去(k-1)B，这样对方只能再减去B，我们得到(A-kB, B)，必胜
2. Theorem: (A, B) is a winning position if and only if A ≥ φ B.

论证过程是：

Round 1: (A, B). If A ≥ 2B, i.e., A/B ≥ 2, then (A, B) is winning.  
Round 2: (B, A-B). If B ≥ 2(A-B), i.e., A/B ≤ 3/2, then (A, B) is losing.  
Round 3: (A-B, 2B-A). If A-B ≥ 2(2B-A), i.e., A/B ≥ 5/3, then (A, B) is wining.  
Round 4: (2B-A, 2A-3B). If 2B-A ≥ 2(2A-3B), i.e., A/B ≤ 8/5, then (A, B) is losing.  
And so on.  
1,2,3,5,8是斐波那契数列，A/B是后项与前项的比值，即φ = (1 + √ 5) / 2。已知A，找出B中小于等于A/φ或者大于等于A*φ的部分。

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


