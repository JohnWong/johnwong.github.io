---
layout: post
title: 1-0组成的串中，1和0个数相等的最长子串
category: past
description: 同学面试遇到的题。
---
同学面试遇到的题，我以尽量简单的方式描述，偶子串这个概念是为了表述创造的概念。

#### Problem

如果一个串只由1和0组成，并且其中1和0的个数相等，我们称之为偶子串。给出一个只由1和0组成的串，求这个串中的子串中，最长的偶子串。

#### Input

第一行是N，测试用例的总数，接下来是N行1和0组成的串

#### Output

N行结果，最长偶子串可能有多

#### Sample

```
Input

5
100111011001
10001111
10010111
100111010011
0111101010101110

Output

Case #1: 10
Case #2: 6
Case #3: 6
Case #4: 10
Case #5: 8
```

解题思路：

先扫描一遍，将0转换成-1，并求出数组的和。和为正则多余1，和为负则多余-1，多出的个数为和的绝对值。我们从数组的前后去掉多余的1或者-1，就找到了可能的最长偶子串。一种特殊的情况是例如，多余1，但是当前数组前后均为-1，我们去掉前面的-1，并且让和+1，从剩下的数组中找。同样去掉后面的-1，和+1，从剩下的数组中找。如果和变为0，就将其放入一个set。最后找出set中长度最长的元素。

不知道这样的方法有没有问题，求指导啊。我把这个解法的整个Java文件贴出来了。

```java
import static java.lang.Math.*;  
import static java.util.Arrays.*;  
import java.io.*;  
import java.util.*;  
  
public class Bin {  
    static boolean LOCAL = System.getSecurityManager() == null;  
    static boolean TO_FILE = true;  
    Scanner sc = new Scanner(System.in);  
  
    void solve(Integer[] data, int start, int end, int distance,  
            Set<Integer[]> set) {  
        // 如果前面的元素与要去掉的相同，则去掉前面的  
        while (data[start] * distance > 0 && start <= end) {  
            distance -= data[start];  
            start++;  
        }  
        // 如果后面的元素与要去掉的相同，则去掉前面的  
        while (data[end] * distance > 0 && start <= end) {  
            distance -= data[end];  
            end--;  
        }  
        // 无法找到偶子串  
        if (start > end)  
            return;  
        // 找到偶子串，将结构放入set  
        if (distance == 0) {  
            set.add(Arrays.copyOfRange(data, start, end + 1));  
            return;  
        } else {  
            // 当前串两端的元素都与要去掉的不相同，则去掉前边一个元素计算，再去掉后边一个元素计算  
            solve(data, start + 1, end, distance - data[start], set);  
            solve(data, start, end - 1, distance - data[end], set);  
        }  
    }  
  
    void run() {  
        int C = sc.nextInt();  
        for (int c = 1; c <= C; c++) {  
            String s = sc.next();  
            Integer[] data = new Integer[s.length()];  
            int total = 0;  
            for (int i = 0; i < s.length(); i++) {  
                data[i] = s.charAt(i) == '1' ? 1 : -1;  
                total += data[i];  
            }  
            Set<Integer[]> result = new HashSet<Integer[]>();  
            solve(data, 0, data.length - 1, total, result);  
            debug(result.toArray());  
            // 找到set中长度最长的元素  
            int max = 0;  
            for (Integer[] i : result) {  
                if (i.length > max)  
                    max = i.length;  
            }  
            System.out.println(String.format("Case #%d: %d", c, max));  
        }  
    }  
  
    void debug(Object... os) {  
        System.err.println(deepToString(os));  
    }  
  
    public static void main(String[] args) {  
        if (LOCAL) {  
            try {  
                System.setIn(new FileInputStream("./bin/intwo.txt"));  
            } catch (Throwable e) {  
                LOCAL = false;  
            }  
        }  
        new Bin().run();  
    }  
} 
```