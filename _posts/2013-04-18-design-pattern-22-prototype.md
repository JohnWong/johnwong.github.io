---
layout: post
title: "设计模式[22]-Prototype"
category: Past
description: 用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。
---
Type: Creational

Prototype:&nbsp;用原型实例指定创建对象的种类，并且通过拷贝这些原型创建新的对象。

```cpp
#include <iostream>
using namespace std;

class Prototype
{
public:
    virtual Prototype* clone()= 0;
    int mType; 
};

class ConcretePrototype: public Prototype
{
public:
    ConcretePrototype* clone()
    {
        ConcretePrototype* pConcretePrototype = new ConcretePrototype;
        pConcretePrototype->mType = this->mType;
        return pConcretePrototype;
    };
};

int main()
{
    Prototype* pPrototype1 = new ConcretePrototype;
    pPrototype1->mType = 47;
    cout<<"pPrototype1 "<<pPrototype1->mType<<endl;
    Prototype* pPrototype2 = pPrototype1->clone();
    cout<<"pPrototype2 "<<pPrototype2->mType<<endl;;
    system("pause");
}

#include <iostream>
using namespace std;

class Prototype
{
public:
    virtual Prototype* clone()= 0;
    int mType; 
};

class ConcretePrototype: public Prototype
{
public:
    ConcretePrototype* clone()
    {
        ConcretePrototype* pConcretePrototype = new ConcretePrototype;
        pConcretePrototype->mType = this->mType;
        return pConcretePrototype;
    };
};

int main()
{
    Prototype* pPrototype1 = new ConcretePrototype;
    pPrototype1->mType = 47;
    cout<<"pPrototype1 "<<pPrototype1->mType<<endl;
    Prototype* pPrototype2 = pPrototype1->clone();
    cout<<"pPrototype2 "<<pPrototype2->mType<<endl;;
    system("pause");
}
```