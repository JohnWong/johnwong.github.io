---
layout: post
title: "[算法]-Longest Increasing Subsequence"
category: past
description: 看微软笔试题遇到的。
---

看微软笔试题遇到的。

> Longest Increasing Subsequence(LIS) means a sequence containing some elements in another sequence by the same order, and the values of elements keeps increasing.For example, LIS of {2,1,4,2,3,7,4,6} is {1,2,3,4,6}, and its LIS length is 5.Considering an array with N elements , what is the lowest time and space complexity to get the length of LIS？

算法一：动态规划

```cpp
#include <iostream>
#include <vector>
using namespace std;
#define SIZE 8 
int s[SIZE]= {2,1,4,2,3,7,4,6};       // sequence
int length[SIZE];  // 第 x 格的值為 s[0...x] 的 LIS 長度
 
void LIS()
{
    // 初始化。每一個數字本身就是長度為一的 LIS。
    for (int i=0; i<SIZE; i++) length[i] = 1;
 
    for (int i=0; i<SIZE; i++)
        // 找出 s[i] 後面能接上哪些數字，
        // 若是可以接，長度就增加。
        for (int j=i+1; j<SIZE; j++)
            if (s[i] < s[j])
                length[j] = max(length[j], length[i] + 1);
 
    // length[] 之中最大的值即為 LIS 的長度。
    int n = 0;
    for (int i=0; i<SIZE; i++)
        n = max(n, length[i]);
    cout << "LIS的長度是" << n;
}

int main(void)  
{  
    LIS();
    system("pause");  
    return 0;  
}
```

算法二：

```CPP
#include <iostream>
#include <vector>
using namespace std;
#define SIZE 8 
int s[SIZE]= {2,1,4,2,3,7,4,6};       // sequence
int b[SIZE];

// num为要查找的数,k是范围上限
// 二分查找大于num的最小值，并返回其位置
int bSearch(int num, int k)  
{  
    int low=1, high=k;  
    while(low<=high)  
    {  
        int mid=(low+high)/2;  
        if(num>=b[mid])  
            low=mid+1;  
        else   
            high=mid-1;  
    }  
    return low;  
}; 

void LIS()
{
	int low = 1, high = SIZE;
	int k = 1;
	b[1] = s[1];
	for(int i=2; i<=SIZE; ++i)
	{
		if(s[i]>=b[k])
			b[++k] = s[i];
		else
		{
			int pos = bSearch(s[i], k);
			b[pos] = s[i];
		}
	}
	printf("%d", k); 
}

int main(void)  
{  
    LIS();
    system("pause");  
    return 0;  
}
```

参考：

http://www.wutianqi.com/?p=1850

http://www.csie.ntnu.edu.tw/~u91029/LongestIncreasingSubsequence.html



