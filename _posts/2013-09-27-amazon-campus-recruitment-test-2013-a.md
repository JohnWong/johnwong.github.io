---
layout: post
title: "2013亚马逊校招机试题A"
category: Past
description: 没通过还错过了有道面试。
---
题目没复制下来，凭印象写的。

删除代码中的的注释。注释分两种，//和/**/。字符串中出现的注释符号不能被当作注释。

解题思路：

以前编译原理课做过类似的程序，分出几个状态，并做状态转移判断即可。

StringBuilder中存放返回的字符串。动作a表示添加当前字符到StringBuilder，b表示删除StringBuilder中最后一个字符。-表示其他字符或者无动作或者状态不转变

| 状态 | 字符 | 转变状态 | 动作 |
| --- | --- | --- | --- |
| 0 | " | 1 | a |
| 0 | / | 2 | a |
| 0 | - | - | a |
| 1 | " | 0 | a |
| 1 | - | - | a |
| 2 | * | 3 | b |
| 2 | / | 4 | b |
| 2 | - | 0 | a |
| 3 | * | 5 | - |
| 3 | - | - | - |
| 4 | \n | 0 | a |
| 4 | - | - | - |
| 5 | / | 0 | - |
| 5 | * | - | - |
| 5 | - | 3 | - |

```java
static void backOne(StringBuilder sb) {  
    sb.delete(sb.length() - 1, sb.length());  
}  
  
static String removeComment(String s) {  
    StringBuilder sb = new StringBuilder();  
    int state = 0;  
    for (int i = 0; i < s.length(); i++) {  
        char c = s.charAt(i);  
        switch (state) {  
        case 0:  
            switch (c) {  
            case '"':  
                sb.append(c);  
                state = 1;  
                break;  
            case '/':  
                sb.append(c);  
                state = 2;  
                break;  
            default:  
                sb.append(c);  
            }  
            break;  
        case 1:  
            switch (c) {  
            case '"':  
                sb.append(c);  
                state = 0;  
                break;  
            default:  
                sb.append(c);  
            }  
            break;  
        case 2:  
            switch (c) {  
            case '*':  
                backOne(sb);  
                state = 3;  
                break;  
            case '/':  
                backOne(sb);  
                state = 4;  
                break;  
            default:  
                sb.append(c);  
                state = 0;  
            }  
            break;  
        case 3:  
            switch (c) {  
            case '*':  
                state = 5;  
                break;  
            }  
            break;  
        case 4:  
            switch (c) {  
            case '\n':  
                sb.append(c);  
                state = 0;  
                break;  
            }  
            break;  
        case 5:  
            switch (c) {  
            case '/':  
                state = 0;  
                break;  
            case '*':  
                break;  
            default:  
                state = 3;  
            }  
        }  
    }  
    return sb.toString();  
} 
```