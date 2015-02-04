---
layout: post
title: 2013编程之美全国挑战赛第一场-树上的三角形
category: Past
description: 喜欢这样的比赛，只是自己能力有限。
---
树上三角形
======

时间限制: 2000ms 内存限制: 256MB

#### 描述
有一棵树，树上有只毛毛虫。它在这棵树上生活了很久，对它的构造了如指掌。所以它在树上从来都是走最短路，不会绕路。它还还特别喜欢三角形，所以当它在树上爬来爬去的时候总会在想，如果把刚才爬过的那几根树枝/树干锯下来，能不能从中选三根出来拼成一个三角形呢？

#### 输入
输入数据的第一行包含一个整数 T，表示数据组数。  
接下来有 T 组数据，每组数据中：  
第一行包含一个整数 N，表示树上节点的个数（从 1 到 N 标号）。  
接下来的 N-1 行包含三个整数 a, b, len，表示有一根长度为 len 的树枝/树干在节点 a 和节点 b 之间。  
接下来一行包含一个整数 M，表示询问数。  
接下来M行每行两个整数 S, T，表示毛毛虫从 S 爬行到了 T，询问这段路程中的树枝/树干是否能拼成三角形。

#### 输出
对于每组数据，先输出一行"Case #X:",其中X为数据组数编号，从 1 开始。  
接下来对于每个询问输出一行，包含"Yes"或“No”，表示是否可以拼成三角形。

#### 数据范围
1 ≤ T ≤ 5  
小数据：1 ≤ N ≤ 100, 1 ≤ M ≤ 100, 1 ≤ len ≤ 10000  
大数据：1 ≤ N ≤ 100000, 1 ≤ M ≤ 100000, 1 ≤ len ≤ 1000000000

#### 样例输入
```
2
5
1 2 5
1 3 20
2 4 30
4 5 15
2
3 4
3 5
5
1 4 32
2 3 100
3 5 45
4 5 60
2
1 4
1 3
```

#### 样例输出
```
Case #1:
No
Yes
Case #2:
No
Yes
```

思路很简单，Dijkstra算法求出最短路径，暂没考虑多条路径的情况。然后三角形判断。可是最后Wrong Answer。

```java
import java.util.ArrayList;  
import java.util.Arrays;  
import java.util.HashMap;  
import java.util.Scanner;  
  
public class Main {  
    public static void main(String[] args) {  
        Scanner in = new Scanner(System.in);  
        int T = in.nextInt();  
        for (int i = 0; i < T; i++) {  
            int N = in.nextInt();  
            int[][] data = new int[N + 1][N + 1];  
            for (int j = 0; j < N - 1; j++) {  
                int from = in.nextInt();  
                int to = in.nextInt();  
                int cost = in.nextInt();  
                data[from][to] = cost;  
                data[to][from] = cost;  
            }  
            int Q = in.nextInt();  
            System.out.println("Case #" + (i+1) + ":");  
            for (int j = 0; j < Q; j++) {  
                int from = in.nextInt();  
                int to = in.nextInt();  
                int[] cost = new int[N + 1];  
                boolean[] isFind = new boolean[N + 1];  
                HashMap<Integer, ArrayList<Integer>> path = new HashMap<Integer, ArrayList<Integer>>();  
                int current = from;  
                isFind[current] = true;  
                // Dijstra from->to  
                for (int l = 1; l < N+1; l++) {  
                    int min = -1;  
                    for (int k = 1; k < N+1; k++) {  
                        if (data[current][k] > 0 && !isFind[k]) {  
                            int temp = cost[current] + data[current][k];  
                            if (cost[k] == 0 || temp < cost[k]) {  
                                ArrayList<Integer> newPath = new ArrayList<Integer>();  
                                newPath.add(data[current][k]);  
                                if (path.get(current) != null) {  
                                    newPath.addAll(path.get(current));  
                                    path.put(k, newPath);  
                                }  
                                path.put(k, newPath);  
                                cost[k] = temp;  
                            }  
                            if (min < 0 || cost[k] < cost[min]) {  
                                min = k;  
                            }  
                        }  
                    }  
                    current = min;  
//                  System.out.println("current:" + current);  
                    if (current < 0) {  
                        break;  
                    } else if (current == to) {  
                        break;  
                    }  
                    isFind[current] = true;  
                }  
                System.out.println(path.get(to));  
                // 寻找  
                if (path.get(to) != null) {  
                    Integer[] pathArray = path.get(to).toArray(new Integer[0]);  
                    boolean find = false;  
                    for (int ii=0; ii<pathArray.length; ii++) {  
                        for(int ij=ii+1;ij<pathArray.length; ij++){  
                            for(int ik=ij+1;ik<pathArray.length;ik++){  
//                              System.out.println("path:" + pathArray[ii] + " " + pathArray[ij] + " " + pathArray[ik]);  
                                if(pathArray[ii] + pathArray[ij] > pathArray[ik]  
                                        && pathArray[ij] + pathArray[ik] > pathArray[ii]  
                                        && pathArray[ik] + pathArray[ii] > pathArray[ij]){  
                                    find = true;  
                                    break;  
                                }  
                            }  
                            if(find)break;  
                        }  
                        if(find)break;  
                    }  
                    if(find)  
                        System.out.println("Yes");  
                    else   
                        System.out.println("No");  
                } else {  
                    System.out.println("No");  
                }  
            }  
        }  
    }  
}
```