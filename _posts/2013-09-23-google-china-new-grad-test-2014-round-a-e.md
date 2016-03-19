---
layout: post
title: "Google China New Grad Test 2014 Round A Problem E"
category: past
description: Google校招留下遗憾。
---
### Problem E. Spaceship Defence

### Problem
The enemy has invaded your spaceship, and only superior tactics will allow you to defend it! To travel around your spaceship, your soldiers will use two devices: teleporters andturbolifts.

Teleporters allow your soldiers to move instantly between rooms. Every room contains a teleporter, and rooms are color-coded: if a soldier is in a room with some color, she can use the teleporter in that room to immediately move to any other room with the same color.

Turbolifts allow your soldiers to move between rooms more slowly. A turbolift is like an elevator that moves in many directions. Each turbolift moves from one room to one other room, and it takes a certain amount of time to travel. Notes about turbolifts:

Turbolifts are not two-way: if a turbolift moves soldiers from room a to room b, the same turbolift cannot move soldiers from room b to room a, although there might be another turbolift that does that.
More than one soldier can use the same turbolift, and they do not interfere with each other in any way.
You will be given the locations and destinations of several soldiers. For each soldier, output the minimum amount of time it could take that soldier to travel from his location to his destination.

### Input
The first line of the input gives the number of test cases, T. T test cases follow.

For every test case:

The first line of every test case contains an integer N, which is the number of rooms in your spaceship. The rooms are numbered from 1 to N. The following N lines each contain a string telling the color of the rooms, from room 1 to room N. The strings only contain characters a-z (the lower-case English letters) and 0-9 (the number 0 to 9), and the length of each string will be less than or equal to 2.

The next line in the test case is an integer M, which indicates the number of turbolifts in your spaceship. The following M lines each contain 3 space-separated integers ai, bi, ti, telling us that there is a turbolift that can transport soldiers from room ai to room bi in tiseconds.

The next line in the test case contains an integer S, which is the number of soldiers at your command. The following S lines each contain two integers: the location and destination of one soldier, pj and qj.

### Output
For each test case, output one line containing only the string "Case #x:", where x is the number of the test case (starting from 1). On the next S lines, output a single integer: on line j, the smallest number of seconds it could take for a soldier to travel from pj to qj. If there is no path from pj to qj, the integer you output should be -1.

### Limits
1 ≤ S ≤ 100.
1 ≤ ai, bi ≤ N.
0 ≤ ti ≤ 1000.
1 ≤ pj, qj ≤ N.
### Small dataset
1 ≤ T ≤ 10.
1 ≤ N ≤ 1000.
0 ≤ M ≤ 3000.
### Large dataset
T = 1.
1 ≤ N ≤ 80000.
0 ≤ M ≤ 3000.
### Sample
```
Input 
 
3
3
gl
t3
t3
3
1 2 217
3 2 567
1 1 21
2
2 1
2 3
4
ca
bl
bl
8z
0
3
1 2
2 3
1 1
8
re
b7
ye
gr
0l
0l
ye
b7
7
4 1 19
2 4 21
2 5 317
4 5 34
4 7 3
4 8 265
8 6 71
3
4 3
2 6
1 4
 	
Output 

Case #1:
-1
0
Case #2:
-1
0
0
Case #3:
3
55
-1
```

解题思路：被题目绕得云里雾里，其实是一个图的最短路径问题。根据输入信息构造好图之后，用Dijikstra算法求最短路径即可。暂时没通过，还没找到问题所在。明天面阿里，希望能在跌倒的地方爬起来。先暂时搁置准备面试。

```java
void run() {  
    int tests = sc.nextInt();  
    for (int test = 1; test <= tests; test++) {  
        int N = sc.nextInt() + 1;  
        debug(N);  
        String[] rooms = new String[N];  
        int[][] graph = new int[N][N];  
        for (int[] z : graph)  
            Arrays.fill(z, -1);  
  
        for (int i = 1; i < N; i++)  
            graph[i][i] = 0;  
  
        for (int i = 1; i < N; i++) {  
            rooms[i] = sc.next();  
            for (int j = 1; j < i; j++)  
                if (rooms[j].equals(rooms[i]))  
                    graph[i][j] = graph[j][i] = 0;  
        }  
        debug(rooms);  
        int M = sc.nextInt();  
        for (int i = 0; i < M; i++) {  
            int a = sc.nextInt();  
            int b = sc.nextInt();  
            int t = sc.nextInt();  
            debug(a, b, t);  
            graph[a][b] = graph[a][b] >= 0 ? min(graph[a][b], t) : t;  
        }  
        int S = sc.nextInt();  
  
        System.out.println(String.format("Case #%d:", test));  
        for (int i = 0; i < S; i++) {  
            int p = sc.nextInt();  
            int q = sc.nextInt();  
            debug(S, p, q);  
            int res = dijkstra(graph, p, q);  
            System.out.println(res);  
        }  
    }  
}  
  
int dijkstra(int[][] graph, int p, int q) {  
    HashSet<Integer> find = new HashSet<Integer>();  
    HashSet<Integer> notFind = new HashSet<Integer>();  
    find.add(p);  
    for (int i = 1; i < graph.length; i++)  
        if (i != p)  
            notFind.add(i);  
    while (true) {  
        int s = -1, e = -1;  
        for (Integer i : find)  
            for (Integer j : notFind)  
                if (graph[i][j] >= 0)  
                    if (s == -1 || graph[i][j] < graph[s][e]) {  
                        s = i;  
                        e = j;  
                    }  
        if(s == -1)  
            break;  
        if(graph[p][e] == -1)  
            graph[p][e] = graph[p][s] + graph[s][e];  
        else  
            graph[p][e] = min(graph[p][e], graph[p][s] + graph[s][e]);  
        notFind.remove(e);  
        find.add(e);  
        if(e==q)  
            break;  
    }  
    return graph[p][q];  
}  
```