---
layout: post
title: "Google 2014校招测试赛 Problem B"
category: Past
description: Google校招测试赛第二题。
---
### Problem B. Captain Hammer

#### Problem

The Hamjet is a true marvel of aircraft engineering. It is a jet airplane with a single engine so powerful that it burns all of its fuel instantly during takeoff. The Hamjet doesn't have any wings because who needs them when the fuselage is made of a special Wonderflonium isotope that makes it impervious to harm.

Piloting the Hamjet is a not a job for your typical, meek-bodied superhero. That's why the Hamjet belongs to Captain Hammer, who is himself impervious to harm. The G-forces that the pilot endures when taking a trip in the Hamjet are legen-dary.

The Hamjet takes off at an angle of θ degrees up and a speed of V meters per second. Vis a fixed value that is determined by the awesome power of the Hamjet engine and the capacity of its fuel tank. The destination is D meters away. Your job is to program the Hamjet's computer to calculate θ given V and D.

Fortunately, the Hamjet's Wondeflonium hull is impervious to air friction. Even more fortunately, the Hamjet doesn't fly too far or too high, so you can assume that the Earth is flat, and that the acceleration due to gravity is a constant 9.8 m/s2 down.

#### Input

The first line of the input gives the number of test cases, T. T lines follow. Each line will contain two positive integers -- V and D.

#### Output

For each test case, output one line containing "Case #x: θ", where x is the case number (starting from 1) and θ is in degrees up from the the horizontal. If there are several possible answers, output the smallest positive one.

An answer will be considered correct if it is within 10-6 of the exact answer, in absolute or relative error. See the FAQ for an explanation of what that means, and what formats of floating-point numbers we accept.

#### Limits

1 ≤ T ≤ 4500;
1 ≤ V ≤ 300;
1 ≤ D ≤ 10000;
It is guaranteed that each test case will be solvable.

#### Sample

```
Input 
 	
3
98 980
98 490
299 1234

Output 
 
Case #1: 45.0000000
Case #2: 15.0000000
Case #3: 3.8870928
```

解法：抛物线已知重力，初速度和距离，求角度。算算公式就行，在精度的问题上碰了钉子。同样的公式用Python和Java得出的结果差0.0000001。重算公式，单步调试，最后还是无法解决。最后直接提交竟然通过了。幸亏没超过要求的精度范围。关键代码如下：

```java
void run() {
	double g = 9.8;
	int COUNT = sc.nextInt();
	for (int c = 0; c < COUNT; c++) {
		double v = sc.nextInt();
		double d = sc.nextInt();
		double x = 0.25 - (d * d * g * g) / (4.0 * v * v * v * v);
		if(x<0&&x>-0.0000000001)
			x = 0;
		x = Math.sqrt(0.5 - Math.sqrt(x));
		double sin = Math.asin(x) * 180 / Math.PI;
		System.out.println(String.format("Case #%d: %.8f", c + 1, sin));
	}
}
```
