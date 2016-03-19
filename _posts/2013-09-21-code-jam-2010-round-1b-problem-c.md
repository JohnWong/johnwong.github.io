---
layout: post
title: "Code Jam 2010 Round 1B Problem C"
category: past
description: Code Jam练习
---
### Problem C. Your Rank is Pure


#### Problem
Pontius: You know, I like this number 127, I don't know why.
Woland: Well, that is an object so pure. You know the prime numbers.
Pontius: Surely I do. Those are the objects possessed by our ancient masters hundreds of years ago. Oh, yes, why then? 127 is indeed a prime number as I was told.
Woland: Not... only... that. 127 is the 31st prime number; then, 31 is itself a prime, it is the 11th; and 11 is the 5th; 5 is the 3rd; 3, you know, is the second; and finally 2 is the 1st.
Pontius: Heh, that is indeed... purely prime.
The game can be played on any subset S of positive integers. A number in S is considered pure with respect to S if, starting from it, you can continue taking its rank in S, and get a number that is also in S, until in finite steps you hit the number 1, which is not in S.

When n is given, in how many ways you can pick S, a subset of {2, 3, ..., n}, so that n is pure, with respect to S? The answer might be a big number, you need to output it modulo 100003.

#### Input
The first line of the input gives the number of test cases, T. T lines follow. Each contains a single integer n.

#### Output
For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is the answer as described above.

#### Limits
T ≤ 100.
Small dataset
2 ≤ n ≤ 25.

#### Large dataset
2 ≤ n ≤ 500.

#### Sample
```
Input
 
2
5
6
 	
Output 

Case #1: 5
Case #2: 8
```

解题思路：花了好多时间在理解题意上。前面讲质数什么的后面其实和质数一点关系也没有。理解之后就是组合问题了。对于某个N，根据S中元素个数计算出多组符合条件的情况，就会发现每一组个数计算的时候可以利用之前的结论。动态规划解决问题。

```java
long[][] memo = new long[501][501];  
long[][] c = new long[501][501];  
final long MOD = 100003;  
  
long calc(int n, int k) {  
    if (memo[n][k] != -1) {  
        return memo[n][k];  
    }  
    if (k == 1 || n - k == 1) {  
        return memo[n][k] = 1;  
    }  
  
    memo[n][k] = 0;  
    for (int j = 1; j < k; j++) {  
        if (n - k >= k - j) {  
            memo[n][k] = (memo[n][k] + calc(k, j) * c[n - k - 1][k - j - 1])  
                    % MOD;  
        }  
    }  
  
    return memo[n][k];  
}  
  
void run() {  
    for (long[] z : memo) {  
        Arrays.fill(z, -1);  
    }  
    c[0][0] = 1;  
    for(int i=1; i<501; i++){  
        c[i][0] = 1;  
        for(int j=1; j<501; j++){  
            c[i][j] = (c[i-1][j-1] + c[i-1][j]) % MOD;  
        }  
    }  
    int tests = sc.nextInt();  
    for (int test = 1; test <= tests; test++) {  
        int N = sc.nextInt();  
        long ret = 0;  
        for(int i=1; i<N; i++)  
            ret = (ret + calc(N, i)) % MOD;  
        System.out.println(String.format("Case #%d: %d", test, ret));  
    }  
}  
```
