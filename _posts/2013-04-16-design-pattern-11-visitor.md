---
layout: post
title: 设计模式[11]-Visitor
category: past
description: 在Java中，Visitor模式实际上是分离了容器中的元素和对这些元素进行操作的行为。
---
Type: Behavioral

Visitor: Visitor提供要对对象结构中元素执行的操作。让你可以在不修改其操作的元素的情况下定义新操作。在元素类型很少改变的情况下适用。

```cpp
#include <iostream>
using namespace std;

class ConcreteElementA;
class ConcreteElementB;
class Visitor
{
public:
    virtual void visitElementA(ConcreteElementA* a) = 0;
    virtual void visitElementB(ConcreteElementB* b) = 0;
};

class Element
{
public:
    virtual void accept(Visitor* v)=0;
};

class ConcreteVisitor: public Visitor
{
public:
    void visitElementA(ConcreteElementA* a)
    {
        cout<<"visitElementA"<<endl;
    };
    void visitElementB(ConcreteElementB* b)
    {
        cout<<"visitElementB"<<endl;
    };
};

class ConcreteElementA: public Element
{
public:
    void accept(Visitor* v)
    {
        v->visitElementA(this); 
    };
};

class ConcreteElementB: public Element
{
public:
    void accept(Visitor* v)
    {
        v->visitElementB(this); 
    };
};

int main()
{
	Visitor *pVisitor = new ConcreteVisitor;
	Element *pElement  = new ConcreteElementA;

	pElement->accept(pVisitor);
	
	pElement = new ConcreteElementB;
	pElement->accept(pVisitor);
	
    system("pause");
	return 0;
}
```