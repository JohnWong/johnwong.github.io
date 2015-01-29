---
layout: post
title: 设计模式[15]-Decorator
category: Past
description: 动态给一个对象添加一些额外的职责。
---

Type: Structural

Decorator: 动态给一个对象添加一些额外的职责，就象在墙上刷油漆。使用Decorator模式相比用生成子类方式达到功能的扩充显得更为灵活。

```java
FileReader fr = new FileReader(filename);
BufferedReader br = new BufferedReader(fr);
```

实际上Java 的I/O API就是使用Decorator实现的,I/O变种很多,如果都采取继承方法,将会产生很多子类,显然相当繁琐.

```cpp
#include <iostream>  
#define Data int  
using namespace std;  
  
class Component  
{  
public:  
    virtual void operation()=0;  
};  
  
class ConcreteComponent: public Component  
{  
public:  
    void operation()  
    {  
        cout<<"ConcreteComponent operation"<<endl;  
    };  
};  
  
class Decorator  
{  
public:  
    virtual void operation() = 0;  
};  
  
class ConcreteDecorator: public Decorator  
{  
public:  
    ConcreteDecorator(Component* pComponent): m_pComponent(pComponent){};  
    void operation()  
    {  
        cout<<"ConcreteDecorator operation"<<endl;  
        addedBehavior();  
    };  
    void addedBehavior()  
    {  
        m_pComponent->operation();  
    };  
private:  
    Data addedState;  
    Component* m_pComponent;  
};  
  
int main()  
{  
    Component* pComponent = new ConcreteComponent();  
    Decorator* pDecorator = new ConcreteDecorator(pComponent);  
  
    pDecorator->operation();  
  
    system("pause");  
  
    return 0;  
} 
```