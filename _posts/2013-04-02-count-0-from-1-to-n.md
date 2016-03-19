---
layout: post
title: 从1到n的正数中0的出现次数
category: past
description: 准备找工作了，上次搞这些算法数据结构还是研究生复试上机考试。现在必须得重操旧业了。
---

准备找工作了，上次搞这些算法数据结构还是研究生复试上机考试。现在必须得重操旧业了。加油！

写的很简单，能实现功能，但是需要改进，接下来再研究。

```cpp
int countZero(int data){
    int count = 0;
    for(int i=1; i<=data; i++){
        int d = i;
        while(d > 0){
            if(d%10 == 0){
                 count ++;
            }
            d=d/10; 
        }
    }
    return count;
}
```