---
layout: post
title: "2013编程之美全国挑战赛第一场-传话游戏"
category: Past
description: 喜欢这样的比赛，只是自己能力有限。
---
传话游戏
======

时间限制: 1000ms 内存限制: 256MB

#### 描述
Alice和Bob还有其他几位好朋友在一起玩传话游戏。这个游戏是这样进行的：首先，所有游戏者按顺序站成一排，Alice站第一位，Bob站最后一位。然后，Alice想一句话悄悄告诉第二位游戏者，第二位游戏者又悄悄地告诉第三位，第三位又告诉第四位……以此类推，直到倒数第二位告诉Bob。两位游戏者在传话中，不能让其他人听到，也不能使用肢体动作来解释。最后，Bob把他所听到的话告诉大家，Alice也把她原本所想的话告诉大家。 

由于传话过程中可能出现一些偏差，游戏者越多，Bob最后听到的话就与Alice所想的越不同。Bob听到的话往往会变成一些很搞笑的东西，所以大家玩得乐此不疲。经过几轮游戏后，Alice注意到在两人传话中，有些词汇往往会错误地变成其他特定的词汇。Alice已经收集到了这样的一个词汇转化的列表，她想知道她的话传到Bob时会变成什么样子，请你写个程序来帮助她。

#### 输入
输入包括多组数据。第一行是整数 T，表示有多少组测试数据。每组数据第一行包括两个整数 N 和 M，分别表示游戏者的数量和单词转化列表长度。随后有 M 行，每行包含两个用空格隔开的单词 a 和 b，表示单词 a 在传话中一定会变成 b。输入数据保证没有重复的 a。最后一行包含若干个用单个空格隔开的单词，表示Alice所想的句子，句子总长不超过100个字符。所有单词都只包含小写字母，并且长度不超过20，同一个单词的不同时态被认为是不同的单词。你可以假定不在列表中的单词永远不会变化。

#### 输出
对于每组测试数据，单独输出一行“Case #c: s”。其中，c 为测试数据编号，s 为Bob所听到的句子。s 的格式与输入数据中Alice所想的句子格式相同。

#### 数据范围
1 ≤ T ≤ 100  
小数据：2 ≤ N ≤ 10, 0 ≤ M ≤ 10  
大数据：2 ≤ N ≤ 100, 0 ≤ M ≤ 100 

#### 样例输入

```
2
4 3
ship sheep
sinking thinking
thinking sinking
the ship is sinking
10 5
tidy tiny
tiger liar
tired tire
tire bear
liar bear
a tidy tiger is tired
```
#### 样例输出

```
Case #1: the sheep is thinking
Case #2: a tiny bear is bear
```

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