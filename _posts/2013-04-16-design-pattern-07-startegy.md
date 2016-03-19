---
layout: post
title: 设计模式[7]-Strategy
category: past
description: 实现算法具体实现和抽象接口之间的解耦。
---

Type: Behavioral

Strategy模式：定义一系列的算法，封装每一个，使他们实现通用。让算法相对于使用他的clients可以独立地变化。

```cpp
#include <iostream>  
using namespace std;  
  
  
class Strategy  
{  
public:  
    virtual void execute() = 0;  
};   
  
  
class ConcreteStrategyA: public Strategy  
{  
public:  
    void execute()  
    {  
        cout<<"ConcreteStrategyA executed"<<endl;  
    }  
};  
  
  
class ConcreteStrategyB: public Strategy  
{  
public:  
    void execute()  
    {  
        cout<<"ConcreteStrategyB executed"<<endl;  
    }  
};  
  
  
class Context  
{  
public:  
    Context (Strategy* pStrategy): m_pStrategy(pStrategy){};  
    void setStrategy(Strategy* pStrategy)  
    {  
        m_pStrategy = pStrategy;  
    }  
    void invoke()  
    {  
        if(m_pStrategy != NULL)  
            m_pStrategy->execute();  
    }  
private:  
    Strategy* m_pStrategy;  
};  
  
  
int main()  
{  
    Strategy* pStrategy = new ConcreteStrategyA();  
    Context*  pContext  = new Context(pStrategy);  
    pContext->invoke();  
    pStrategy = new ConcreteStrategyB();  
    pContext->setStrategy(pStrategy);  
    pContext->invoke();  
  
    system("pause");  
    return 0;  
}
```