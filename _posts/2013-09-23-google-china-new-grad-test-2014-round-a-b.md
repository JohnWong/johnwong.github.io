---
layout: post
title: "Google China New Grad Test 2014 Round A Problem B"
category: past
description: Google校招留下遗憾。
---
### Problem B. Rational Number Tree


#### Problem
Consider an infinite complete binary tree where the root node is 1/1 and left and right childs of node p/q are p/(p+q) and (p+q)/q, respectively. This tree looks like:

```
         1/1
    ______|______
    |           |
   1/2         2/1
 ___|___     ___|___
 |     |     |     |
1/3   3/2   2/3   3/1
...
```

It is known that every positive rational number appears exactly once in this tree. A level-order traversal of the tree results in the following array:
1/1, 1/2, 2/1, 1/3, 3/2, 2/3, 3/1, ...
Please solve the following two questions:

Find the n-th element of the array, where n starts from 1. For example, for the input 2, the correct output is 1/2.
Given p/q, find its position in the array. As an example, the input 1/2 results in the output 2.

#### Input
The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of one line. The line contains a problem id (1 or 2) and one or two additional integers:

If the problem id is 1, then only one integer n is given, and you are expected to find the n-th element of the array.
If the problem id is 2, then two integers p and q are given, and you are expected to find the position of p/q in the array.

#### Output
For each test case:

If the problem id is 1, then output one line containing "Case #x: p q", where x is the case number (starting from 1), and p, q are numerator and denominator of the asked array element, respectively.
If the problem id is 2, then output one line containing "Case #x: n", where x is the case number (starting from 1), and n is the position of the given number.

#### Limits
1 ≤ T ≤ 100; p and q are relatively prime.

#### Small dataset
1 ≤ n, p, q ≤ 216-1; p/q is an element in a tree with level number ≤ 16.

#### Large dataset
1 ≤ n, p, q ≤ 264-1; p/q is an element in a tree with level number ≤ 64.

#### Sample
```
Input  
 
4
1 2
2 1 2
1 5
2 3 2
 	
Output

Case #1: 1 2
Case #2: 2
Case #3: 3 2
Case #4: 5
```

解题思路：这题太遗憾了。匆忙之中提交大数据，结果发现数据超出long范围，尽快用BigInteger改写，刚好超过了提交时间。也是一道水题，找出推导的方法，递归求解就可以了。

```java
BigInteger findPQ(BigInteger p, BigInteger q) {  
    if (p.equals(new BigInteger("1")) && q.equals(new BigInteger("1")))  
        return new BigInteger("1");  
    if (p.compareTo(q) < 0)  
        return findPQ(p, q.subtract(p)).multiply(new BigInteger("2"));  
    else  
        return findPQ(p.subtract(q), q).multiply(new BigInteger("2")).add(new BigInteger("1"));  
}  
  
BigInteger[] findN(BigInteger n) {  
    BigInteger[] ret = new BigInteger[2];  
    if (n.intValue() == 1) {  
        ret[0] = new BigInteger("1");  
        ret[1] = new BigInteger("1");  
        return ret;  
    }  
    BigInteger p = n.divide(new BigInteger("2"));  
    BigInteger[] pr = findN(p);  
    if (n.equals(p.multiply(new BigInteger("2")))) {  
        // left  
        ret[0] = pr[0];  
        ret[1] = pr[0].add(pr[1]);  
        return ret;  
    } else {  
        // right  
        ret[0] = pr[0].add(pr[1]);  
        ret[1] = pr[1];  
        return ret;  
    }  
  
}  
  
void run() {  
    int tests = sc.nextInt();  
    for (int test = 1; test <= tests; test++) {  
        int id = sc.nextInt();  
        System.out.print(String.format("Case #%d:", test));  
        if (id == 1) {  
            BigInteger n = new BigInteger(sc.next());  
            for (BigInteger i : findN(n)) {  
                System.out.print(" " + i);  
            }  
            System.out.println();  
        } else {  
            BigInteger p = new BigInteger(sc.next());  
            BigInteger q = new BigInteger(sc.next());  
            BigInteger res = findPQ(p, q);  
            System.out.println(" " + res);  
        }  
    }  
}
```