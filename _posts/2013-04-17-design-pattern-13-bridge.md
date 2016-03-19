---
layout: post
title: 设计模式[13]-Bridge
category: past
description: 将抽象部分与实现部分分离，使它们都可以独立的变化。
---
Type: Structural

Bridge: 将抽象与其实现解耦，这样两者可以独立地变化。

```cpp
#include <iostream>
using namespace std;

class Implementor
{
public:
    virtual void operationImpl() = 0;
};

class ConcreteImplementorA: public Implementor
{
public:
    void operationImpl()
    {
        cout<<"ConcreteImplementorA operationImpl"<<endl;
    };
};

class ConcreteImplementorB: public Implementor
{
public:
    void operationImpl()
    {
        cout<<"ConcreteImplementorB operationImpl"<<endl;
    };
};

class Abstraction
{
public:
    void setImplementor(Implementor* pImplementor)
    {
        m_pImplementor = pImplementor;
    };
    void operation()
    {
        if(m_pImplementor != NULL)
            m_pImplementor->operationImpl();
    };
private:
    Implementor* m_pImplementor;
};

int main()
{
    ConcreteImplementorA *pImplA = new ConcreteImplementorA();
    ConcreteImplementorB *pImplB = new ConcreteImplementorB();
    Abstraction *pAbstraction = new Abstraction;
    pAbstraction->setImplementor(pImplA);
    pAbstraction->operation();
    pAbstraction->setImplementor(pImplB);
    pAbstraction->operation();

    system("pause");
    return 0;
}
```