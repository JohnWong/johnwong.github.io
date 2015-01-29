---
layout: post
title: "设计模式[19]-Abstract Factory"
category: Past
description: 提供一个接口创建一系列相关或者依赖的对象，而无需指定其实现类。
---
Type: Creational

Abstract Factory: 提供一个接口创建一系列相关或者依赖的对象，而无需指定其实现类。

如果没有应对“多系列对象构建”的需求变化，则没有必要使用Abstract Factory模式。Abstract Factory模式主要在于应对“新系列”的需求变动。缺点是难以应对“新对象”的需求变动。Abstract Factory模式经常和Factory Method模式共同组合来应对“对象创建”的需求变化。

```cpp
#include <iostream>
using namespace std;

class AbstractProductA{};

class AbstractProductB{};

class ConcreteProductA1: public AbstractProductA{
public:
    ConcreteProductA1()
    {
        cout<<"ConcreteProductA1"<<endl;
    };
};

class ConcreteProductB1: public AbstractProductB
{
public:
    ConcreteProductB1()
    {
        cout<<"ConcreteProductB1"<<endl;
    };
};

class ConcreteProductA2: public AbstractProductA
{
public:
    ConcreteProductA2()
    {
        cout<<"ConcreteProductA2"<<endl;
    };
};

class ConcreteProductB2: public AbstractProductB
{
public:
    ConcreteProductB2()
    {
        cout<<"ConcreteProductB2"<<endl;
    };
};

class AbstractFactory
{
public:
    virtual AbstractProductA* createProductA()=0;
    virtual AbstractProductB* createProductB()=0;
};

class ConcreteFactory1: public AbstractFactory
{
public:
    AbstractProductA* createProductA()
    {
        return new ConcreteProductA1;
    };
    AbstractProductB* createProductB()
    {
        return new ConcreteProductB1;
    };
};

class ConcreteFactory2: public AbstractFactory
{
public:
    AbstractProductA* createProductA()
    {
        return new ConcreteProductA2;
    };
    AbstractProductB* createProductB()
    {
        return new ConcreteProductB2;
    };
};

int main()
{
	ConcreteFactory1 *pFactory1 = new ConcreteFactory1;
	AbstractProductA *pProductA = pFactory1->createProductA();
	AbstractProductB *pProductB = pFactory1->createProductB();
    
    ConcreteFactory2 *pFactory2 = new ConcreteFactory2;
    pProductA = pFactory2->createProductA();
    pProductB = pFactory2->createProductB();

    system("pause");
    return 0;
}
```