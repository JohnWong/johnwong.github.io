---
layout: post
title: CareerCup-BASE CASE AND BUILD
category: past
description: 这个题刷起来感觉比编程之美什么的easy多了。
---

这个题刷起来感觉比编程之美什么的easy多了。

Description: 

Solve the algorithm first for a base case (e g , just one element) Then, try to solve it for elements one and two, assuming that you have the answer for element one Then, try to solve it for elements one, two and three, assuming that you have the answer to elements one and two 

Example: 

Design an algorithm to print all permutations of a string For simplicity, assume all characters are unique.

Testing String: abcdefg

Case “a” --> {a}
Case “ab” --> {ab, ba}
Case “abc” --> ?

```cpp
#include <iostream>  
using namespace std;  
  
void print(char* prefix, char* data, int index, int length)  
{  
     if(index >= length)  
     {  
         static int count = 0;  
         printf("%d: %s\n", count++, prefix);  
         return;  
     }  
     int prelength = strlen(prefix);  
     for(int i=0; i<prelength+1; i++)  
     {  
         char* s = new char[prelength + 2];;  
         int count = 0, j;  
         for(j=0; j<prelength+1; j++)  
         {  
             if(j == i)  
                 s[j] = data[index];  
             else  
                 s[j] = prefix[count++];  
         }  
         s[j] = '\0';  
         print(s, data, index+1, length);  
     }  
};  
  
int main()  
{  
    char* data = "abcd";  
    print("", data, 0, strlen(data));  
    system("pause");   
};  
```