---
layout: post
title: 设计模式[23]-Singleton
category: Past
description: 保证一个类只有一个示例，并且提供一个全局指针指向他。
---

Type: Creational

Singleton: 保证一个类只有一个示例，并且提供一个全局指针指向他。Singleton也能够被无状态化。提供工具性质的功能。

```cpp
#include <iostream>  
using namespace std;  
  
class Singleton  
{  
public:  
    static Singleton* instance()  
    {  
        static Singleton uniqueInstance;  
        return &uniqueInstance;  
    };  
private:  
    Singleton()    
    {    
        cout<<"Singleton"<<endl;    
    };   
    static string singletonData;  
};  
  
int main()  
{  
    Singleton* pInstance1 = Singleton::instance();  
    Singleton* pInstance2 = Singleton::instance();  
    cout<<"Address compare: "<<boolalpha<<(pInstance1 == pInstance2)<<endl;  
    system("pause");      
}
```

设计模式学习完了。花了好几天的时间。感觉自己理解的还很肤浅。想要学透，只能在实践中慢慢体会。解道网是个很不错的网站，以后要学会从更大的角度思考问题。明天开始抓紧看看面试题，准备微软的面试。加油！