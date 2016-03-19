---
layout: post
title: 设计模式[10]-Mediator
category: past
description: 通过中间人来促进松散耦合。
---
Type: Behavioral

Mediator: 定义一个对象，包装一系列对象如何交互。这些对象不必明确地互相引用，从而促进松散耦合，并且能够使你独立地改变他们之间的交互。

```cpp
#include <iostream>
using namespace std;

class Mediator
{
public:
    virtual void inform(int id)=0;
};


class Colleague
{
public:
    virtual void update()=0;
};


class ConcreteColleague: public Colleague
{
public:
    ConcreteColleague(int id, Mediator* pMediator): mId(id),m_pMediator(pMediator){};
    void update()
    {
        cout<<"ConcreteColleague"<<mId<<"update"<<endl;
    };
    void send()
    {
        cout<<"ConcreteColleague"<<mId<<"send"<<endl;
        if(mId == 1)
            m_pMediator->inform(2);
        else if(mId == 2)
            m_pMediator->inform(1);
    };
private:
    int mId;
    Mediator* m_pMediator; 
};


class ConcreteMediator: public Mediator
{
public:
    void inform(int id)
    {
        if(id==1){
            m_pColleague1->update();
        } else if(id == 2){
            m_pColleague2->update();
        }
    };
    void setColleague1(Colleague* pColleague)
    {
        m_pColleague1 = pColleague;
    };
    void setColleague2(Colleague* pColleague)
    {
        m_pColleague2 = pColleague;
    };
private:
    Colleague* m_pColleague1;
    Colleague* m_pColleague2;
};


int main()
{
    ConcreteMediator* pMediator = new ConcreteMediator();
    ConcreteColleague* pColleague1 = new ConcreteColleague(1, pMediator);
    ConcreteColleague* pColleague2 = new ConcreteColleague(2, pMediator);
    pMediator->setColleague1(pColleague1);
    pMediator->setColleague2(pColleague2);    pColleague1->send();
    pColleague2->send();    system("pause");
    return 0;
}
```














