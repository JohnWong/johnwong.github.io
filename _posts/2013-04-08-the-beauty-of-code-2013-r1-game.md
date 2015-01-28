---
layout: post
title: "2013编程之美全国挑战赛第一场-传话游戏"
category: Past
description: 喜欢这样的比赛，只是自己能力有限。
---
[题目](http://programming2013.cstnet.cn/qualification/problem/1)

题目很简单，理解上开始没注意到N的作用。

```Java
import java.util.HashMap;
import java.util.Scanner;


public class Ex1 {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int count = in.nextInt();
		for (int i = 0; i < count; i++) {
			int N = in.nextInt();
			int M = in.nextInt();
			HashMap<String, String> map = new HashMap<String, String>();
			for (int j = 0; j < M; j++) {
				map.put(in.next(), in.next());
			}
			in.nextLine();
			String[] sentence = in.nextLine().split(" ");


			System.out.print("Case #" + (i + 1) + ":");
			for(int j=0; j<sentence.length; j++){
				if(map.containsKey(sentence[j])){
					String word = map.get(sentence[j]);
					for (int k = 0; k < N - 2;k++){
						if(map.containsKey(word)){
							word = map.get(word);
						} else {
							break;
						}
					}
					System.out.print(" " + word);
				} else {
					System.out.print(" " + sentence[j]);
				}
			}
			System.out.println();
		}
	}
}
```