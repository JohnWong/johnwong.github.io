---
layout: post
title: "东京大学ACM Java模板"
category: past
description: 工欲善其事，必先利其器。模版在手可以将注意力放在问题本身。
---
```java
import static java.lang.Math.*;
import static java.util.Arrays.*;
import java.io.*;
import java.util.*;

public class Main {
	static boolean LOCAL = System.getSecurityManager() == null;
	static boolean TO_FILE = true;
	Scanner sc = new Scanner(System.in);

	void run() {

	}

	void debug(Object... os) {
		System.err.println(deepToString(os));
	}

	public static void main(String[] args) {
		if (LOCAL) {
			try {
				System.setIn(new FileInputStream("./bin/in.txt"));
			} catch (Throwable e) {
				LOCAL = false;
			}
		}
		if (TO_FILE) {
			try {
				System.setOut(new PrintStream("./src/output.txt"));
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			}
		}
		new Main().run();
	}
}
```