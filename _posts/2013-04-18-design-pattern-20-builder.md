---
layout: post
title: "设计模式[20]-Builder"
category: Past
description: 将一个复杂对象的构建与它的表示分离,使得同样的构建过程可以创建不同的表示
---
Type: Creational

Builder: 将一个复杂对象的构建与它的表示分离,使得同样的构建过程可以创建不同的表示。是为了将构建复杂对象的过程和它的部件解耦。Builder负责构建部件，Director负责处理构建的过程。

```cpp
#include <iostream>
using namespace std;

class Part{};

class Product
{
public:
    Product(Part* pPartA, Part* pPartB, Part* pPartC){};
};

class Builder
{
public:
    virtual void buildPartA()=0;
    virtual void buildPartB()=0;
    virtual void buildPartC()=0;
};

class ConcreteBuilder: public Builder
{
public:
    void buildPartA()
    {
        cout<<"Build Part A"<<endl;
        mPartA = new Part;
    };
    void buildPartB()
    {
        cout<<"Build Part B"<<endl;
        mPartB = new Part;
    };
    void buildPartC()
    {
        cout<<"Build Part C"<<endl;
        mPartC = new Part;
    };
    Product* getResult()
    {
        cout<<"Get Result"<<endl;
        return new Product(mPartA, mPartB, mPartC);
    };
private:
    Part *mPartA, *mPartB, *mPartC;
};

class Director
{
public:
    Director(Builder* pBuilder):m_pBuilder(pBuilder){};
    void construct()
    {
        cout<<"Director construct"<<endl;
        m_pBuilder->buildPartA();
        m_pBuilder->buildPartB();
        m_pBuilder->buildPartC();
    };
private:
    Builder* m_pBuilder;
};

int main()
{
    ConcreteBuilder* pBuilder = new ConcreteBuilder;
    Director *pDirector = new Director(pBuilder);
    pDirector->construct();
    pBuilder->getResult();

    system("pause");

    return 0;
}
```