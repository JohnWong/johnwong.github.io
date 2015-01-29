---
layout: post
title: "Code Jam 2010 Round 1A Problem A"
category: Past
description: Code Jam练习
---
[https://code.google.com/codejam/contest/544101/dashboard#s=p0](https://code.google.com/codejam/contest/544101/dashboard#s=p0)

### Problem A. Rotate

#### Problem

In the exciting game of Join-K, red and blue pieces are dropped into an N-by-N table. The table stands up vertically so that pieces drop down to the bottom-most empty slots in their column. For example, consider the following two configurations:

```
    - Legal Position -

          .......
          .......
          .......
          ....R..
          ...RB..
          ..BRB..
          .RBBR..
```

```
   - Illegal Position -

          .......
          .......
          .......
          .......
   Bad -> ..BR...
          ...R...
          .RBBR..
```

In these pictures, each '.' represents an empty slot, each 'R' represents a slot filled with a red piece, and each 'B' represents a slot filled with a blue piece. The left configuration is legal, but the right one is not. This is because one of the pieces in the third column (marked with the arrow) has not fallen down to the empty slot below it.

A player wins if they can place at least K pieces of their color in a row, either horizontally, vertically, or diagonally. The four possible orientations are shown below:

```
      - Four in a row -

     R   RRRR    R   R
     R          R     R
     R         R       R
     R        R         R
```

In the "Legal Position" diagram at the beginning of the problem statement, both players had lined up two pieces in a row, but not three.
As it turns out, you are right now playing a very exciting game of Join-K, and you have a tricky plan to ensure victory! When your opponent is not looking, you are going to rotate the board 90 degrees clockwise onto its side. Gravity will then cause the pieces to fall down into a new position as shown below:

```
    - Start -

     .......
     .......
     .......
     ...R...
     ...RB..
     ..BRB..
     .RBBR..
```

```
   - Rotate -

     .......
     R......
     BB.....
     BRRR...
     RBB....
     .......
     .......
```

```
   - Gravity -

     .......
     .......
     .......
     R......
     BB.....
     BRR....
     RBBR...
```

Unfortunately, you only have time to rotate once before your opponent will notice.
All that remains is picking the right time to make your move. Given a board position, you should determine which player (or players!) will have K pieces in a row after you rotate the board clockwise and gravity takes effect in the new direction.

#### Notes

* You can rotate the board only once.
* Assume that gravity only takes effect after the board has been rotated completely.
* Only check for winners after gravity has finished taking effect.

#### Input

The first line of the input gives the number of test cases, T. T test cases follow, each beginning with a line containing the integers N and K. The next N lines will each be exactly N characters long, showing the initial position of the board, using the same format as the diagrams above.

The initial position in each test case will be a legal position that can occur during a game of Join-K. In particular, neither player will have already formed K pieces in a row.

#### Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1), and y is one of "Red", "Blue", "Neither", or "Both". Here, y indicates which player or players will have K pieces in a row after you rotate the board.

#### Limits

1 ≤ T ≤ 100.
3 ≤ K ≤ N.

#### Small dataset

3 ≤ N ≤ 7.

#### Large dataset

3 ≤ N ≤ 50.

Sample

```
Input
 
4
7 3
.......
.......
.......
...R...
...BB..
..BRB..
.RRBR..
6 4
......
......
.R...R
.R..BB
.R.RBR
RB.BBB
4 4
R...
BR..
BR..
BR..
3 3
B..
RB.
RB.
 	
Output 

Case #1: Neither
Case #2: Both
Case #3: Red
Case #4: Blue
```

解题思路：

先将矩阵旋转，然后在横向、纵向和两个斜向查找。根据旋转后的性质，可以在适当的地方提前退出。斜向检查的横纵坐标会麻烦一些。开始犯的错误是没有检查另一个斜向。

```java
int[][] rotate(char[][] d) {
	int[][] ret = new int[d.length][d.length];
	for (int i = d.length - 1; i >= 0; i--) {
		int rx = d.length - 1;
		boolean hasMore = false;
		for (int j = d.length - 1; j >= 0; j--) {
			if (d[i][j] == 'R' || d[i][j] == 'B') {
				ret[rx][d.length - 1 - i] = d[i][j] == 'R' ? 1 : 2;
				rx--;
				hasMore = true;
			}
		}
		if (!hasMore)
			break;
	}
	return ret;
}

// H check
int checkWinH(int[][] d, int k) {
	int winner = 0;
	for (int i = d.length - 1; i >= 0; i--) {
		int current = 0;
		int count = 0;
		boolean hasMore = false;
		for (int j = 0; j < d.length; j++) {
			System.err.print(d[i][j]);
			if (d[i][j] > 0)
				hasMore = true;
			if (d[i][j] != current) {
				current = d[i][j];
				count = 1;
			} else {
				count++;
				if (count >= k) {
					winner |= current;
					if(winner == 3)
						return winner;
				}
			}
		}
		System.err.println();
		if (!hasMore)
			break;
	}
	return winner;
}

// V check
int checkWinV(int[][] d, int k) {
	int winner = 0;
	for (int j = 0; j < d.length; j++) {
		int current = 0;
		int count = 0;
		boolean hasMore = false;
		for (int i = d.length - 1; i >= 0; i--) {
			if (d[i][j] > 0)
				hasMore = true;
			if (d[i][j] != current) {
				current = d[i][j];
				count = 1;
			} else {
				count++;
				if (count >= k) {
					winner |= current;
					if(winner == 3)
						return winner;
				}
			}
		}
		if (!hasMore)
			break;
	}
	return winner;
}

// D check
int checkWinD(int[][] d, int k) {
	int winner = 0;
	for (int j = d.length - k; j >= 0; j--) {
		int current = 0;
		int count = 0;
		for (int i = 0, oj = j; oj < d.length; i++, oj++) {
			System.err.print(d[i][oj]);
			if (d[i][oj] != current) {
				current = d[i][oj];
				count = 1;
			} else {
				count++;
				if (count >= k) {
					winner |= current;
					if(winner == 3)
						return winner;
				}
			}
		}
		System.err.println();
	}
	for (int i = 1; i <= d.length - k; i++) {
		int current = 0;
		int count = 0;
		for (int j = 0, oi = i; oi < d.length; j++, oi++) {
			System.err.print(d[oi][j]);
			if (d[oi][j] != current) {
				current = d[oi][j];
				count = 1;
			} else {
				count++;
				if (count >= k) {
					winner |= current;
					if(winner == 3)
						return winner;
				}
			}
		}
		System.err.println();
	}

	for (int i = k-1; i<d.length; i++) {
		int current = 0;
		int count = 0;
		for (int j = 0, oi = i; oi >= 0; j++, oi--) {
			System.err.print(d[oi][j]);
			if (d[oi][j] != current) {
				current = d[oi][j];
				count = 1;
			} else {
				count++;
				if (count >= k) {
					winner |= current;
					if(winner == 3)
						return winner;
				}
			}
		}
		System.err.println();
	}
	for (int j = 1; j <= d.length - k; j++) {
		int current = 0;
		int count = 0;
		for (int i = d.length - 1, oj = j; oj < d.length; oj++, i--) {
			System.err.print(d[i][oj]);
			if (d[i][oj] != current) {
				current = d[i][oj];
				count = 1;
			} else {
				count++;
				if (count >= k) {
					winner |= current;
					if(winner == 3)
						return winner;
				}
			}
		}
		System.err.println();
	}
	return winner;
}

void run() {
	int COUNT = sc.nextInt();
	for (int c = 0; c < COUNT; c++) {
		int t = sc.nextInt();
		int k = sc.nextInt();
		char[][] ori = new char[t][t];
		for (int i = 0; i < t; i++) {
			String s = sc.next();
			for (int j = 0; j < t; j++) {
				ori[i][j] = s.charAt(j);
			}
		}
		int[][] tar = rotate(ori);
		print(tar);
		debug(c+1);
		int result = checkWinH(tar, k);
		if(result != 3)
			result |= checkWinV(tar, k);
		if(result != 3)
			result |= checkWinD(tar, k);
		String s = "Neither";
		if (result == 1)
			s = "Red";
		else if (result == 2)
			s = "Blue";
		else if (result == 3)
			s = "Both";
		System.out.println(String.format("Case #%d: %s", c + 1, s));
	}
}
```
