---
layout: post
title: "Google China New Grad Test 2014 Round A Problem C"
category: Past
description: Google校招留下遗憾。
---
### Problem C. Sorting


#### Problem
Alex and Bob are brothers and they both enjoy reading very much. They have widely different tastes on books so they keep their own books separately. However, their father thinks it is good to promote exchanges if they can put their books together. Thus he has bought an one-row bookshelf for them today and put all his sons' books on it in random order. He labeled each position of the bookshelf the owner of the corresponding book ('Alex' or 'Bob').

Unfortunately, Alex and Bob went outside and didn't know what their father did. When they were back, they came to realize the problem: they usually arranged their books in their own orders, but the books seem to be in a great mess on the bookshelf now. They have to sort them right now!!

Each book has its own worth, which is represented by an integer. Books with odd values of worth belong to Alex and the books with even values of worth belong to Bob. Alex has a habit of sorting his books from the left to the right in an increasing order of worths, while Bob prefers to sort his books from the left to the right in a decreasing order of worths.

At the same time, they do not want to change the positions of the labels, so that after they have finished sorting the books according their rules, each book's owner's name should match with the label in its position.

Here comes the problem. A sequence of N values s0, s1, ..., sN-1 is given, which indicates the worths of the books from the left to the right on the bookshelf currently. Please help the brothers to find out the sequence of worths after sorting such that it satisfies the above description.

#### Input
The first line of input contains a single integer T, the number of test cases. Each test case starts with a line containing an integer N, the number of books on the bookshelf. The next line contains N integers separated by spaces, representing s0, s1, ..., sN-1, which are the worths of the books.

#### Output
For each test case, output one line containing "Case #X: ", followed by t0, t1, ..., tN-1 in order, and separated by spaces. X is the test case number (starting from 1) and t0, t1, ...,tN-1 forms the resulting sequence of worths of the books from the left to the right.

#### Limits
1 ≤ T ≤ 30.

#### Small dataset
1 ≤ N ≤ 100
-100 ≤ si ≤ 100

#### Large dataset
1 ≤ N ≤ 1000
-1000 ≤ si ≤ 1000

#### Sample
```
Input
 
2
5
5 2 4 3 1
7
-5 -12 87 2 88 20 11
 	
Output 

Case #1: 1 4 2 3 5
Case #2: -5 88 11 20 2 -12 87
```

解题思路：还是道水题。对一个数组中奇数和偶数分别进行排序，要求之前放奇数的位置仍然是奇数。快排定位纯奇数会比较麻烦，数据量也不大，所以选择了冒泡排序。

```java
void run() {
    int tests = sc.nextInt();
    for (int test = 1; test <= tests; test++) {
        int N = sc.nextInt();
        int[] s = new int[N];
        for (int i = 0; i < N; i++) {
            s[i] = sc.nextInt();
        }
        for (int j = 0; j < N; j++) {
            int op = -1, ep = -1;
            for (int i = 0; i < N; i++) {
                if (s[i] % 2 == 1 || s[i] % 2 == -1) { // odd
                    if (op != -1) {
                        if (s[i] < s[op])
                            swap(s, i, op);
                    }
                    op = i;
                } else {
                    if (ep != -1) {
                        if (s[i] > s[ep])
                            swap(s, i, ep);
                    }
                    ep = i;
                }
            }
        }
        System.out.print(String.format("Case #%d:", test));
        for(int i=0; i<N; i++){
            System.out.print(" " + s[i]);
        }
        System.out.println();  

    }
}
```