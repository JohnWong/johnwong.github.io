---
layout: post
title: 设计模式[21]-Factory Method
category: Mobile
---

Type: Creational

Factory Method: 定义一个创建对象的接口，但是让子类决定实例化那个类。新增加一个产品的时候，只需派生一个该类型的工厂而无需修改原来的代码。每个具体工厂只负责返回一种产品类。是最典型的模板方法模式(Templete Method pattern)应用。

```c++
#include <iostream>  
using namespace std;  
  
class Product{};  
  
class ConcreteProduct: public Product  
{  
public:  
    ConcreteProduct()  
    {  
        cout<<"ConcreteProduct"<<endl;  
    };  
};  
  
class Creator  
{  
public:  
    virtual Product* factoryMethod() = 0;  
};  
  
class ConcreteCreator: public Creator  
{  
public:  
    Product* factoryMethod()  
    {  
        cout<<"ConcreteCreator decide which class to instantiate"<<endl;  
        return new ConcreteProduct;  
    };  
};  
  
int main()  
{  
    Creator* pCreator = new ConcreteCreator;  
    Product* pProduct = pCreator->factoryMethod();  
    system("pause");  
}; 
```