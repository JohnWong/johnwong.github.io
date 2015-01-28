---
layout: post
title: 设计模式[3]-Observer
category: Past
description: 观察者模式：在对象间定义一对多的依赖关系，这样当一个对象改变状态时，自动通知更新依赖他的对象。
---
Type: Behavioral

观察者模式：在对象间定义一对多的依赖关系，这样当一个对象改变状态时，自动通知更新依赖他的对象。

```CPP
#include <iostream>
#include <list>

using namespace std;
 
typedef int STATE;

class Observer
{
public:
	virtual void update(STATE state) = 0;
};

class ConcreteObserver : public Observer
{
public:
	void update(STATE state){
        cout<<"Update Observer State:"<<state<<endl; 
        observerState = state; 
    };
private:
    STATE observerState; 
};

class Subject
{
public:
	virtual void notify();
	void attach(Observer *pObserver){
        m_ListObserver.push_back(pObserver);
    };
	void detach(Observer *pObserver){
        list<Observer*>::iterator iter;
    	iter = find(m_ListObserver.begin(), m_ListObserver.end(), pObserver);
    	if (m_ListObserver.end() != iter)
    	{
    		m_ListObserver.erase(iter);
    	}
    };

protected:
	list<Observer*> m_ListObserver;
};

class ConcreteSubject : public Subject
{
public:
    void notify(){
        list<Observer*>::iterator list_it;
    	for (list_it = m_ListObserver.begin(); list_it != m_ListObserver.end();
    		 ++list_it)
    	{
    		(*list_it)->update(subjectState);
    	}
    };
    void setState(STATE state){
        subjectState = state;
    };
private:
    STATE subjectState;
};

int main()
{
    Observer *p1 = new ConcreteObserver;
	Observer *p2 = new ConcreteObserver;

	ConcreteSubject* p = new ConcreteSubject;
	p->attach(p1);
	p->attach(p2);
	p->setState(4);
	p->notify();

	p->detach(p1);
	p->setState(10);
	p->notify();
	system("pause");
	return 0;
}
```