---
layout: post
title: "Google China New Grad Test 2014 Round A Problem D"
category: past
description: Google校招留下遗憾。
---
### Problem D. Cross the maze

#### Problem
Edison, a robot, does not have a right hand or eyes. As a brave robot, he always puts his left hand on the wall no matter he walks or turns around. Because he thinks it is too dangerous, Edison does not walk backward.

Assume that Edison has found himself in a square-shaped maze of NxN square cells which is surrounded by walls from the outside. In the maze, some of the cells are also walls. Edison can only move between two empty cells in four directions, north, south, west and east. In order to get out of the maze, he drafts a plan. He uses his left hand to lean on the wall and goes by following the wall.

Here is the question, is Edison able to get out of the maze in at most 10,000 steps? If he can make it, output the path. By getting out of the maze, he only needs to be in the exit cell. If the starting cell is the same as the exit, Edison won't need to move and can directly get out of the maze.

#### Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case starts with an integer N. N is the size of the maze. The following N lines, each line contains N characters which may be '.' or '#'. '.' is an empty cell, '#' is a wall. Followed by a line which contains four integers: sx, sy, ex, ey. (sx, sy) means that Edison is standing on row sx and column sy as his starting cell, (ex, ey) is the exit of the maze. (sx, sy) is guaranteed to be at one of the 4 corners of the maze, and Edison can only touch the wall on 4 adjacent cells(not 8) initially. (ex, ey) can be anywhere in the maze. Note that the top-left corner is at position (1,1).

#### Output
For each test case, output a line containing "Case #x: y", where x is the case number (starting from 1) and y is "Edison ran out of energy." (without the quotes) if Edison can't reach the exit of the maze in at most 10,000 steps, otherwise y should be the number of steps followed by another line which contains y characters to describe the path (each character should be E for east, S for south, W for west or N for north). There is no character to represent the turning around. We don't care about the turning around steps, please only output the path of how Edison will cross the maze.

#### Limits
1 ≤ T ≤ 30.
1 ≤ sx, sy, ex, ey ≤ N.
The starting cell and the exit of the maze will always be an empty cell. And the starting cell and the exit of the maze won't be the same.

#### Small dataset
2 ≤ N ≤ 10.

#### Large dataset
2 ≤ N ≤ 100.

#### Sample
```
Input 
 
3
2
.#
#.
1 1 2 2
5
.##.#
.....
...#.
.###.
...#.
1 1 5 3
3
...
.#.
...
1 1 3 3
 
Output

Case #1: Edison ran out of energy.
Case #2: 22
SEEENSESSSNNNWWSWWSSEE
Case #3: 4
EESS
```

> Note: 
> 
> In the 2nd test case after moving 1 cell down from his starting cell, Edison will still be able to lean on the wall at the cell (1,2) by his left hand.   
> In the third test case, due to Edison can't touch the wall at cell (2,2) initially, so he has to go east in his first step.

解题思路：看到机器人路径的问题就头大了，没在规定时间内做完。比赛结束去买饭的时候才想明白，这题其实很简单。机器人不能后退和只有左手，实际上大大降低了题目难度。事实上机器人的走路的方式很简单，就是在一个#包围的空间内，贴着边界顺时针方向行走。不需要借助递归，因为始终只有一条路可走。动作只有两种：

1. 根据所扶的墙向前走；  
2. 无法向前走时原地顺时针方向转向，寻找新的墙。

```java
void run() {  
    int tests = sc.nextInt();  
    for (int test = 1; test <= tests; test++) {  
        int n = sc.nextInt();  
        char[][] a = new char[n + 2][n + 2];  
        Arrays.fill(a[0], '#');  
        for (int i = 1; i <= n; i++) {  
            a[i][0] = '#';  
            String s = sc.next();  
            for (int j = 1; j <= n; j++)  
                a[i][j] = s.charAt(j - 1);  
            a[i][n + 1] = '#';  
        }  
        Arrays.fill(a[n + 1], '#');  
        int sx = sc.nextInt();  
        int sy = sc.nextInt();  
        int ex = sc.nextInt();  
        int ey = sc.nextInt();  
        System.out.print(String.format("Case #%d: ", test));  
        int stx = sx, sty = sy;  
        if(sx == 1)  
            if(sy == 1)  
                stx--;  
            else  
                sty++;  
        else  
            if(sy == 1)  
                sty--;  
            else  
                stx++;  
              
        find(a, sx, sy, ex, ey, stx, sty);  
    }  
}  
  
int[] go(char[][] a, int x, int y, int wx, int wy) {  
    int[] ret = null;// = new int[]{x, y};  
    if ((x == wx || x == wx - 1) && y == wy - 1 && x + 1 < a.length  
            && a[x + 1][y] == '.') {  
        ret = new int[] { x + 1, y, 2 };// S  
    }  
    if ((x == wx || x == wx + 1) && y == wy + 1 && x - 1 > 0  
            && a[x - 1][y] == '.') {  
        ret = new int[] { x - 1, y, 0 };// N  
    }  
    if ((y == wy || y == wy - 1) && x == wx + 1 && y + 1 < a.length  
            && a[x][y + 1] == '.') {  
        ret = new int[] { x, y + 1, 1 };// E  
    }  
    if ((y == wy || y == wy + 1) && x == wx - 1 && y - 1 > 0  
            && a[x][y - 1] == '.') {  
        ret = new int[] { x, y - 1, 3 };// W  
    }  
    debug("GO", x, y, wx, wy, ret);  
    return ret;  
}  
  
int[] turn(char[][] a, int x, int y, int wx, int wy) {  
    int[] ret = null;  
    if ((wx == x || wx == x - 1) && wy == y - 1) {  
        ret = new int[] { x - 1, y, 1, }; // N  
    } else if (wx == x - 1 && (wy == y || wy == y + 1)) {  
        ret = new int[] { x, y + 1, 2 }; // E  
    } else if ((wx == x || wx == x + 1) && wy == y + 1) {  
        ret = new int[] { x + 1, y, 3 }; // S  
    } else if (wx == x + 1 && (wy == y || wy == y - 1)) {  
        ret = new int[] { x, y - 1, 4 }; // W  
    }  
    debug("TURN", x, y, wx, wy, ret);  
    return ret;  
}  
  
static char[] DIR = new char[] { 'N', 'E', 'S', 'W' };  
  
private void find(char[][] a, int sx, int sy, int ex, int ey, int wx, int wy) {  
    int x = sx, y = sy;  
    int[][] dirs = new int[a.length][a.length];  
    StringBuilder sb = new StringBuilder();  
    while (true) {  
        if (x == ex && y == ey) {  
            System.out.println(sb.length());  
            System.out.println(sb.toString());  
            return;  
        }  
        int[] goRes = go(a, x, y, wx, wy);  
        if (goRes != null) {  
            x = goRes[0];  
            y = goRes[1];  
            sb.append(DIR[goRes[2]]);  
        } else {  
            int[] tRes = turn(a, x, y, wx, wy);  
            if (tRes == null)  
                break;  
            else {  
                wx = tRes[0];  
                wy = tRes[1];  
                int dir = tRes[2];  
                if ((dirs[x][y] & 1 << dir) > 0) {  
                    break;  
                } else {  
                    dirs[x][y] |= 1 << dir;  
                }  
            }  
        }  
    }  
    System.out.println("Edison ran out of energy.");  
} 
```