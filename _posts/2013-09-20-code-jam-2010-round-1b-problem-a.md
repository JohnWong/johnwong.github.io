---
layout: post
title: "Code Jam 2010 Round 1B Problem A"
category: past
description: Code Jam练习
---
### Problem B. Picking Up Chicks

#### Problem
A flock of chickens are running east along a straight, narrow road. Each one is running with its own constant speed. Whenever a chick catches up to the one in front of it, it has to slow down and follow at the speed of the other chick. You are in a mobile crane behind the flock, chasing the chicks towards the barn at the end of the road. The arm of the crane allows you to pick up any chick momentarily, let the chick behind it pass underneath and place the picked up chick back down. This operation takes no time and can only be performed on a pair of chicks that are immediately next to each other, even if 3 or more chicks are in a row, one after the other.

Given the initial locations (Xi) at time 0 and natural speeds (Vi) of the chicks, as well as the location of the barn (B), what is the minimum number of swaps you need to perform with your crane in order to have at least K of the N chicks arrive at the barn no later than time T?

You may think of the chicks as points moving along a line. Even if 3 or more chicks are at the same location, next to each other, picking up one of them will only let one of the other two pass through. Any swap is instantaneous, which means that you may perform multiple swaps at the same time, but each one will count as a separate swap.

#### Input
The first line of the input gives the number of test cases, C. C test cases follow. Each test case starts with 4 integers on a line -- N, K, B and T. The next line contains the Ndifferent integers Xi, in increasing order. The line after that contains the N integers Vi. All distances are in meters; all speeds are in meters per second; all times are in seconds.

#### Output
For each test case, output one line containing "Case #x: S", where x is the case number (starting from 1) and S is the smallest number of required swaps, or the word "IMPOSSIBLE".

#### Limits
1 ≤ C ≤ 100;
1 ≤ B ≤ 1,000,000,000;
1 ≤ T ≤ 1,000;
0 ≤ Xi < B;
1 ≤ Vi ≤ 100;
All the Xi's will be distinct and in increasing order.

#### Small dataset
1 ≤ N ≤ 10;
0 ≤ K ≤ min(3, N);

#### Large dataset
1 ≤ N ≤ 50;
0 ≤ K ≤ N;

#### Sample

```
Input 
 
3
5 3 10 5
0 2 5 6 7
1 1 1 1 4
5 3 10 5
0 2 3 5 7
2 1 1 1 4
5 3 10 5
0 2 3 4 7
2 1 1 1 4
 	
Output

Case #1: 0
Case #2: 2
Case #3: IMPOSSIBLE
```

解题思路：一道多叉树水题。跟之前做的电话号码匹配类似，而且更简单。

```java
class Prefix {
	Map<String, Prefix> sub = new HashMap<String, Prefix>();

	int put(String s) {
		if (s.length() == 0)
			return 0;
		int index = s.indexOf('/', 1);
		if (index < 0)
			index = s.length();
		String s1 = s.substring(0, index);
		String s2 = s.substring(index);
		int ret = 0;
		if (!sub.containsKey(s1)) {
			Prefix child = new Prefix();
			sub.put(s1, child);
			ret++;
		}
		return ret + sub.get(s1).put(s2);
	}
}

void run() {
	int C = sc.nextInt();
	for (int c = 1; c <= C; c++) {
		int N = sc.nextInt();
		int M = sc.nextInt();
		Prefix prefix = new Prefix();
		for (int i = 0; i < N; i++) {
			prefix.put(sc.next());
		}
		int count = 0;
		for (int i = 0; i < M; i++) {
			count += prefix.put(sc.next());
		}
		System.out.println(String.format("Case #%d: %d", c, count));
	}
}
```
