---
layout: post
title: 设计模式[9]-Template Method
category: Past
description: 将算法的一些步骤推迟到子类中实现。
---

Type: Behavioral

Template Method: 在一个操作中定义一个算法的骨架，将一些步骤推迟到子类中。让子类在不修改算法结构的基础上重新定义其中步骤。

```c++
#include <iostream>  
using namespace std;  
  
class AbstractClass  
{  
public:  
    void templateMethod()  
    {  
        cout<<"AbstractClass: Call subMethod"<<endl;  
        subMethod();  
    };  
protected:  
    virtual void subMethod();  
};  
  
class ConcreteClass: public AbstractClass  
{  
public:  
    void subMethod()  
    {  
        cout<<"ConcreteClass: subMethod"<<endl;  
    };  
};  
  
int main()  
{  
    ConcreteClass* pConcreteClass = new ConcreteClass;  
    pConcreteClass->templateMethod();  
  
    system("pause");  
  
    return 0;  
}
```