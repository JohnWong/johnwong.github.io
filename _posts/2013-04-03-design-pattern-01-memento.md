---
layout: post
title: 设计模式[1]-Memento
category: Past
description: 开始研究设计模式。
---
开始研究设计模式。一个非常perfect的设计模式示意图http://www.mcdonaldland.info/2007/11/28/40/

Type: Behavioral

Memento：模式在不破坏封装性的情况下，捕获一个对象的内部状态传递到外部，使得稍后可以将该对象恢复到这个状态。代码参考了http://www.cppblog.com/converse/archive/2006/08/09/11063.html

```cpp
#include <iostream>
#include <string>
using namespace std;
typedef std::string State;

class Originator;

class Memento{
      
private:
    friend class Originator;
    Memento(const State&; rState): state(rState){};
	State state;
};

class Originator
{
public:
    Originator(const State&; rState): state(rState){}
	Memento* createMemento(){
        return new Memento(state);
    }
	void setMemento(Memento* pMemento){
        state = pMemento->state; 
    }
	void printState(){
        cout<<"State:"<<state<<endl;
    }
    void setState(const State&; rState){
        state = rState;
    }

private:
	State state;
};

int main()
{
	// 创建一个原发器
	Originator* pOriginator = new Originator("old state");
	pOriginator->printState();

	// 创建一个备忘录存放这个原发器的状态
	Memento *pMemento = pOriginator->createMemento();
	
	// 更改原发器的状态
	pOriginator->setState("new state");
	pOriginator->printState();

	// 通过备忘录把原发器的状态还原到之前的状态
	pOriginator->setMemento(pMemento);
	pOriginator->printState();

    system("Pause");
	return 0;
}
```