---
layout: post
title: "Code Jam练习"
category: past
description: 今年Google笔试用Code Jam。今天试试怎么用。
---
今年Google笔试用Code Jam。今天试试怎么用。这东西很威武啊，支持各种语言，只要免费许可的都可以，还可以下载别人提交的code。做了几个非常简单的，结果就遇到坑了。

[https://code.google.com/codejam/contest/189252/dashboard](https://code.google.com/codejam/contest/189252/dashboard)

第一道题很简单，将一些字母数字的组合翻译成十进制，类似IEEE754的float格式。需要注意的是，使得到的数字最小，则首位字符对应0，第2个与首位不同的字符对应0。

``` java
public long readFormat(String s) {
	int[] map = new int[256];
	int used = 0;
	for (int i = 0; i < s.length(); i++) {
		char c = s.charAt(i);
		if (map[c] == 0) {
		used++;
		map[c] = used;
		}
	}
	int radix = used;
	if (radix == 1)
		radix = 2;
	long ret = 0;
	for (int i = 0; i < s.length(); i++) {
		char c = s.charAt(i);
		int num = map[c];
		if (num == 1) {
		} else if (num == 2) {
		num = 0;
		} else {
		num--;
		}
		ret *= radix;
		ret += num;
	}
	return ret;
}

void run() {
	int COUNT = sc.nextInt();
	for (int c = 0; c < COUNT; c++) {
		String s = sc.next();
		System.out.println(String.format("Case #%d: %d", c + 1,
			readFormat(s)));
	}
}
```

第二道是几何问题，也不难。最后计算长度的时候遇到问题。这个长度可以用速度乘以时间算出来，同时这个长度也是直角三角形的一个边，也可以根据勾股定律用另两条边求出来。我按照第一个方法提交失败，按照第二个方法，就成功了。

``` java
class Pos {
	double x, y, z;

	public Pos() {
	}

	public Pos(int x, int y, int z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}

	public void add(Pos p) {
		this.x += p.x;
		this.y += p.y;
		this.z += p.z;
	}

	public void divide(double d) {
		this.x /= d;
		this.y /= d;
		this.z /= d;
	}

	public double multiply(Pos p) {
		return this.x * p.x + this.y * p.y + this.z * p.z;
	}

	public Pos multiply(double d) {
		this.x *= d;
		this.y *= d;
		this.z *= d;
		return this;
	}

	public double getDistanceSqare() {
		return x * x + y * y + z * z;
	}

	public double getDistance() {
		debug(getDistanceSqare());
		return sqrt(getDistanceSqare());
	}
}

class Fly {
	Pos p = new Pos();
	Pos v = new Pos();

	public void add(Fly fl) {
		p.add(fl.p);
		v.add(fl.v);
	}

	public void divide(int d) {
		p.divide(d);
		v.divide(d);
	}

	@Override
	public String toString() {
		return "x: " + p.x + " y: " + p.y + " z: " + p.z + " vx: " + v.x
				+ " vy: " + v.y + " vz: " + v.z;
	}
}

void run() {
	int COUNT = sc.nextInt();
	for (int c = 0; c < COUNT; c++) {
		int cc = sc.nextInt();
		Fly center = new Fly();
		for (int i = 0; i < cc; i++) {
			Fly fl = new Fly();
			fl.p.x = sc.nextInt();
			fl.p.y = sc.nextInt();
			fl.p.z = sc.nextInt();
			fl.v.x = sc.nextInt();
			fl.v.y = sc.nextInt();
			fl.v.z = sc.nextInt();
			center.add(fl);
		}
		center.divide(cc);
		debug(center);
		double dotResult = -center.p.multiply(center.v);
		double distance = 0;
		double time = 0;
		if (dotResult <= Double.MIN_VALUE) {
			distance = center.p.getDistance();
		} else {
			double vDisSqare = center.v.getDistanceSqare();
			time = dotResult / vDisSqare;
			distance = center.p.getDistanceSqare()
					- center.v.getDistanceSqare() * time * time;
			if (distance < 0)
				distance = 0;
			else
				distance = sqrt(distance);
		}
		System.out.println(String.format("Case #%d: %.8f %.8f", c + 1,
			distance, time));
	}
}
```



