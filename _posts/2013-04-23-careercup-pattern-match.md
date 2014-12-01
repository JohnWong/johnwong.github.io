---
layout: post
title:  CareerCup-PATTERN MATCHING
category: Mobile
---

CareerCup是一本相当好Code面试的书，开始研读

Description: 

Consider what problems the algorithm is similar to, and figure out if you can modify the solution to develop an algorithm for this problem 

Example:

 A sorted array has been rotated so that the elements might appear in the order 3 4 5 6 7 1 2 How would you find the minimum element?


``` c++
#include <iostream>  
using namespace std;  
  
int find(int* data, int low, int high)  
{  
    printf("%d->%d\n", low, high);  
    if(low == high)  
        return data[low];  
    if(data[low] < data[high])  
        return data[low];  
    int mid = (low + high)/2;  
    if(data[mid] >= data[low])  
        return find(data, mid+1, high);  
    else  
        return find(data, low, mid);  
};   
  
int main()  
{  
    int data[] = {3, 4, 5, 6, 7, 1, 2};  
    printf("%d", find(data, 0, sizeof(data)/sizeof(int)-1));  
    system("pause");   
};  
```