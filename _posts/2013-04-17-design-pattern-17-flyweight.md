---
layout: post
title:  设计模式[17]-Flyweight
category: past
description: 避免大量拥有相同内容的小类的开销，使大家共享一个类。
---

Type: Structural
Flyweight: 避免大量拥有相同内容的小类的开销(如耗费内存)，使大家共享一个类(元类)。找出这些对象群的共同点,设计一个元类，封装可以被共享的类。另外，还有一些特性是取决于应用(context)，是不可共享的，这也Flyweight中两个重要概念内部状态intrinsic和外部状态extrinsic之分。

``` c++
#include <iostream>  
#include <map>   
using namespace std;  
#define State int  
  
class Flyweight   
{  
public:  
    virtual void operation(State extrinsicState) = 0;  
};  
  
class ConcreteFlyweight: public Flyweight  
{  
public:  
    ConcreteFlyweight(State key):intrinsicState(key){};  
    void operation(State extrinsicState)   
    {  
        cout<<"ConcreteFlyweight intrinsicState:"<<intrinsicState  
            <<" extrinsicState"<<extrinsicState<<endl;  
    };  
private:  
    State intrinsicState;  
};  
  
class UnsharedConcreteFlyweight: public Flyweight  
{  
public:  
    void operation(State extrinsicState)   
    {   
        cout<<"UnsharedConcreteFlyweight"<<endl;  
    };  
private:  
    State allState;  
};  
  
class FlyweightFactory  
{  
public:  
    Flyweight* getFlyweight(State key)  
    {  
        Flyweight* pFlyweight = m_Flyweights[key];  
        if(pFlyweight == NULL)  
        {  
            pFlyweight = new ConcreteFlyweight(key);  
            m_Flyweights[key] = pFlyweight;  
        }  
        return pFlyweight;  
    };  
private:  
    map<State, Flyweight*> m_Flyweights;  
};  
  
int main()  
{  
    FlyweightFactory flyweightfactory;  
    flyweightfactory.getFlyweight(0)->operation(0);  
    flyweightfactory.getFlyweight(1)->operation(0);  
  
    system("pause");  
    return 0;  
}
```