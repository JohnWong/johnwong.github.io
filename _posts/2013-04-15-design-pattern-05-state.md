---
layout: post
title: 设计模式[5]-State
category: past
description: 状态模式
---
Type: Behavioral

State模式：允许一个对象在其内部状态改变的时候改变其行为。

```cpp
#include <iostream>
using namespace std;
class State;


class Context
{
public:
    Context(State* pState): mState(pState){};
    void request();
    void setState(State* pState);
private:
    State *mState;
};


class State
{
public:
    virtual void handle(Context* pContext) = 0;
};


class ConcreteState1: public State
{
public:
    void handle(Context* pContext);
};


class ConcreteState2: public State
{
public:
    void handle(Context *pContext);
};


void Context:: request()
{
    mState->handle(this);
}
void Context:: setState(State* pState){
    delete(this->mState);
    this->mState = pState;
}


void ConcreteState1::handle(Context *pContext)
{
    cout<<"Handled by ConcreteState1"<<endl;        
    pContext->setState(new ConcreteState2());
}


void ConcreteState2::handle(Context *pContext)
{
    cout<<"Handled by ConcreteState2"<<endl;        
    pContext->setState(new ConcreteState1());
}


int main()
{
	Context *pContext = new Context(new ConcreteState1);
	pContext->request();
	pContext->request();
    pContext->request();


    delete(pContext);
    system("pause");
	return 0;
}
```