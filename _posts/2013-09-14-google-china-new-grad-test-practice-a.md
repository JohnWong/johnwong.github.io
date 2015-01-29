---
layout: post
title: "Google 2014校招测试赛 Problem A"
category: Past
description: Google校招测试赛第一题。
---
### Problem A. Bad Horse

#### Problem

As the leader of the Evil League of Evil, Bad Horse has a lot of problems to deal with. Most recently, there have been far too many arguments and far too much backstabbing in the League, so much so that Bad Horse has decided to split the league into two departments in order to separate troublesome members. Being the Thoroughbred of Sin, Bad Horse isn't about to spend his valuable time figuring out how to split the League members by himself. That what he's got you -- his loyal henchman -- for.

#### Input

The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with a positive integer M on a line by itself -- the number of troublesome pairs of League members. The next M lines each contain a pair of names, separated by a single space.

#### Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is either "Yes" or "No", depending on whether the League members mentioned in the input can be split into two groups with neither of the groups containing a troublesome pair.

#### Limits

1 ≤ T ≤ 100.  
Each member name will consist of only letters and the underscore character.  
Names are case-sensitive.  
No pair will appear more than once in the same test case.  
Each pair will contain two distinct League members.  

#### Small dataset

1 ≤ M ≤ 10.

#### Large dataset

1 ≤ M ≤ 100.

#### Sample

```
Input  
2
1
Dead_Bowie Fake_Thomas_Jefferson
3
Dead_Bowie Fake_Thomas_Jefferson
Fake_Thomas_Jefferson Fury_Leika
Fury_Leika Dead_Bowie
 	
Output
Case #1: Yes
Case #2: No
```

我的解法是，将数据放入list中。

1. 先取出一对记录，分别放入set1和set2。并且将两个记录分别放入stack1和stack2。

2. 然后从stack1中逐个取出元素，对每个元素执行的操作是，从list中取出还有这个元素的一堆记录，然后将一对中的另一个放入set2和stack2。

3. 然后对stack2执行类似2的操作，一对中另一个放入set1和stack1。

4. 重复执行2和3直到stack1和stack2空。

5. 重复执行1,2,3,4直到list空

6. 检测set1和set2中是否有相同的元素。

关键代码如下：

``` java
boolean solve(List<String> list) {
	Set<String> set1 = new HashSet<String>();
	Set<String> set2 = new HashSet<String>();
	Stack<String> stack1 = new Stack<String>();
	Stack<String> stack2 = new Stack<String>();
	while (list.size() > 0) {
		String p1 = list.get(0);
		list.remove(0);
		String p2 = list.get(0);
		list.remove(0);
		set1.add(p1);
		set2.add(p2);
		stack1.push(p1);
		stack2.push(p2);
		while (!stack1.empty() || !stack2.empty()) {
			if (!stack1.empty()) {
				String s1 = stack1.pop();
				int index = list.indexOf(s1);
				while (index >= 0) {
					String s2;
					if (index % 2 == 1) {
						s2 = list.get(index - 1);
						list.remove(index - 1);
						list.remove(index - 1);
					} else {
						s2 = list.get(index + 1);
						list.remove(index);
						list.remove(index);
					}
					stack2.push(s2);
					set2.add(s2);
					index = list.indexOf(s1);
				}
			}
			if (!stack2.empty()) {
				String s1 = stack2.pop();
				int index = list.indexOf(s1);
				while (index >= 0) {
					String s2;
					if (index % 2 == 1) {
						s2 = list.get(index - 1);
						list.remove(index);
						list.remove(index - 1);
					} else {
						s2 = list.get(index + 1);
						list.remove(index + 1);
						list.remove(index);
					}
					stack1.push(s2);
					set1.add(s2);
					index = list.indexOf(s1);
				}
			}
		}
	}
	System.err.println("comapre set");
	// set1 与set2是否有相同元素
	for (String s : set1) {
		if (set2.contains(s))
			return false;
	}
	return true;
}

void run() {
	int COUNT = sc.nextInt();
	for (int c = 0; c < COUNT; c++) {
		int M = sc.nextInt();
		List<String> list = new ArrayList<String>();
		for (int m = 0; m < M; m++) {
			String p1 = sc.next();
			String p2 = sc.next();
			list.add(p1);
			list.add(p2);
		}
		boolean result = solve(list);
		System.out.println(String.format("Case #%d: %s", c + 1,
			result ? "Yes" : "No"));
	}
}
```



