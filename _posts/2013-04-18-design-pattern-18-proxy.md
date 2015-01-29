---
layout: post
title: 设计模式[18]-Proxy
category: Past
description: 提供一个替代品或者占位符来控制对一个对象的访问。
---

Type: Structural
Proxy: 提供一个替代品或者占位符来控制对一个对象的访问。

```cpp
#include <iostream>  
using namespace std;  
  
class Subject  
{  
public:  
    virtual void request()=0;  
};   
  
class RealSubject: public Subject  
{  
public:  
    void request()  
    {  
        cout<<"Real request"<<endl;  
    }  
};  
  
class Proxy: public Subject  
{  
public:  
    Proxy(RealSubject* pRealSubject):m_pRealSubject(pRealSubject){};  
    void request()  
    {  
        cout<<"Proxy request"<<endl;  
        m_pRealSubject->request();  
    };  
private:  
    RealSubject* m_pRealSubject;  
};  
  
int main()  
{  
    RealSubject* pRealSubject = new RealSubject;  
    Subject* pProxy = new Proxy(pRealSubject);  
    pProxy->request();  
  
    system("pause");  
    return 0;  
} 
```