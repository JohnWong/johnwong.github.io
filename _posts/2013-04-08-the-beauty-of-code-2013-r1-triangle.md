---
layout: post
title: 2013编程之美全国挑战赛第一场-树上的三角形
category: Past
description: 喜欢这样的比赛，只是自己能力有限。
---

[题目](http://programming2013.cstnet.cn/qualification/problem/3)

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