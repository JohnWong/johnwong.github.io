---
layout: post
title: 设计模式[12]-Adapter
category: Mobile
---

Type: Structural

Adapter: 将一个类的接口转换成clients期望的另一个接口。类不会因为接口不兼容而无法一起工作。 实现方式有两种，继承和委让。这里使用的是委让。

``` c++
#include <iostream>  
using namespace std;  
  
class Adapter  
{  
public:  
    virtual void operation()=0;  
};  
  
class Adaptee  
{  
public:  
    void adaptedOperation()  
    {  
        cout<<"adaptedOperation"<<endl;  
    };  
};  
  
class ConcreteAdapter: public Adapter  
{  
public:  
    ConcreteAdapter(Adaptee* pAdaptee):m_pAdaptee(pAdaptee){};  
    void operation()  
    {  
        cout<<"ConcreteAdapter operation"<<endl;  
        m_pAdaptee->adaptedOperation();  
    };  
private:  
    Adaptee* m_pAdaptee;  
};  
  
int main()  
{  
    Adaptee *pAdaptee = new Adaptee;  
    Adapter *pTarget = new ConcreteAdapter(pAdaptee);  
    pTarget->operation();  
  
    system("pause");  
  
    return 0;  
} 
```