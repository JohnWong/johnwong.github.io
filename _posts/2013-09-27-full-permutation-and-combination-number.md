---
layout: post
title: "不使用递归求全排列和组合数"
category: past
description: 经典面试题。
---
同学遇到的面试问题，大意是M台机器放在N个房间，不使用递归求打印所有情况

解题思路：情况共计N**M种。开始想将所有情况放入数组，填充好数组再逐个打印。随后发现按照填充的思路，不使用大数组也可以实现。思路是加入M=N=3，则27种情况，记i0...i26。0...M个数，0放入i0[0],i1[1],i2[2],i3[0],i4[1],i5[2]...，1放入i0[,i1,i2,

| 房间0 | 房间1 | 房间2 |
| --- | --- | --- |
| 0 1 2 | | |
| 1 2 | 0 | |
| 1 2 | | 0 |
| 0 2 | 1 | |
| 2 | 0 1 | |
| 2 | 1 | 0 |
| 0 2 | | 1 |
| 2 | 0 | 1 |
| 2 | | 0 1 |
| 0 1 | 2 | |
| 1 | 0 2 | |
| 1 | 2 | 0 |
| 0 | 1 2 | |
| | 0 1 2 | |
| | 1 2 | 0 |
| 0 | 2 | 1 |
| | 0 2 | 1 |
| | 2 | 0 1 |

```java
/*  
 * 非递归打印全排列。 
 */  
public class Permutations {  
  
    static void swap(char[] s, int i, int j) {  
        char c = s[i];  
        s[i] = s[j];  
        s[j] = c;  
    }  
  
    static void fullPermutation(char[] s) {  
        for (int i = 0; i < s.length; i++) {  
            for (int j = 1; j < s.length; j++) {  
                swap(s, j, j - 1);  
                System.out.println(s);  
            }  
        }  
    }  
  
    public static void main(String[] args) {  
        fullPermutation("1234".toCharArray());  
    }  
}  
```

类似的问题非递归打印组合数。例如Cmn。建立长度为m的数组，前n个置为1。从左到右扫描数组元素值的10组合，找到第一个10组合后将其变为01并将其左边的1移动到最左端。

```java
/* 
 * 非递归打印组合数 
 */  
public class Combinations {  
  
    static void swap(int[] a, int i, int j) {  
        int t = a[i];  
        a[i] = a[j];  
        a[j] = t;  
    }  
  
    static void print(char[] s, int[] t) {  
        for (int i = 0; i < t.length; i++) {  
            if (t[i] == 1)  
                System.out.print(s[i] + " ");  
        }  
        System.out.println();  
    }  
  
    public static void combinations(char[] s, int n) {  
        int[] t = new int[s.length];  
        int m = t.length;  
        for (int i = 0; i < n; i++)  
            t[i] = 1;  
        print(s, t);  
        while (true) {  
            int i;  
            for (i = 1; i < m; i++) {  
                if (t[i] == 0 && t[i - 1] == 1) {  
                    swap(t, i, i - 1);  
                    int p = -1;  
                    for (int j = 0; j < i - 1; j++) {  
                        if (t[j] == 1) {  
                            swap(t, ++p, j);  
                        }  
                    }  
                    print(s, t);  
                    break;  
                }  
            }  
            if (i == m) {  
                return;  
            }  
        }  
    }  
  
    public static void main(String[] args) {  
        char[] s = "12345".toCharArray();  
        combinations(s, 2);  
    }  
}  
```