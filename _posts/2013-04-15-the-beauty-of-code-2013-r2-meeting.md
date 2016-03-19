---
layout: post
title: 2013编程之美全国挑战赛第二场-集会
category: past
description: 思路是对的，遗憾没AC。
---

昨天做编程之美的题感觉只有这一道是水题。思路没问题但是写程序写错了一个地方没AC。今天翻出来想了一下终于解决了。

解题思路： 

要寻找的这个目标点的纵坐标为0，设横坐标为x。以示例数据为例，可以得到目标点到这些点的距离，更直观一点，绘制成图形点击查看。观察可知符合要求的点可能出现的位置是某两个抛物线的交点或者某个抛物线的顶点。求出这些点来比较计算出的距离，取最小的即可。没机会提交的代码如下：

```java
import java.util.Scanner;  
  
public class Main {  
    public static void main(String[] args) {  
        Scanner in = new Scanner(System.in);  
        int T = in.nextInt();// T个测试  
        for (int t = 0; t < T; t++) {  
            int N = in.nextInt();  
            int x[] = new int[N];  
            int y[] = new int[N];  
            for (int i = 0; i < N; i++) {  
                x[i] = in.nextInt();  
                y[i] = in.nextInt();  
            }  
            double min = Double.MAX_VALUE;  
            double ret = 0;  
            for (int i = 0; i < N; i++) {  
                for (int j = i + 1; j < N; j++) {  
                    double d = 0.5  
                            * (sq(x[i]) - sq(x[j]) + sq(y[i]) - sq(y[j]))  
                            / (x[i] - x[j]);  
                    double res = calc(x, y, d);  
                    if (res < min) {  
                        min = res;  
                        ret = d;  
                    }  
                }  
            }  
            for (int i = 0; i < N; i++) {  
                double d = x[i];  
                double res = calc(x, y, d);  
                if (res < min) {  
                    min = res;  
                    ret = d;  
                }  
            }  
            System.out.println("Case #" + (t + 1) + ": " + ret);  
        }  
    }  
  
    public static int sq(int x) {  
        return x * x;  
    }  
  
    public static double sq(double x) {  
        return x * x;  
    }  
  
    public static double calc(int[] x, int[] y, double d) {  
        double max = 0.0;  
        for (int i = 0; i < x.length; i++) {  
            double temp = sq(x[i] - d) + sq(y[i]);  
            if (temp > max)  
                max = temp;  
        }  
        return max;  
    }  
}
```