---
layout: post
title: 设计模式[4]-Command
category: past
description: 将调用操作的对象和知道如何实现该操作的对象解耦。
---
Type: Behavioral

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Receiver
{
public:
    void action()
    {
        cout <<"Receiver Action"<<endl;;
    }
};

class Command
{
public:
    virtual void execute()=0;
};

class ConcreteCommand: public Command
{
public:
    ConcreteCommand(Receiver* pReceiver): m_pReceiver(pReceiver){};
    void execute()
    {
        m_pReceiver->action();
    };
private:
    Receiver* m_pReceiver;
};

class Invoker
{
public:
	void addCommand(Command *pCommand)
	{
        mCommand.push_back(pCommand);
        pCommand->execute();
    }
private:
	vector<Command*> mCommand;
};

int main()
{
	Receiver* pReceiver = new Receiver();
	Command*  pCommand  = new ConcreteCommand(pReceiver);
	Invoker*  pInvoker  = new Invoker();
    pInvoker->addCommand(pCommand);


	system("pause");
	return 0;
}
```
