---
layout: post
title: 设计模式[14]-Composite
category: past
description: 将对象组合成树形结构以表示“部分-整体”的层次结构。
---
Type: Structural
Composite: 通过递归手段来构造诸如文件系统之类的树形的对象结构；Composite模式所代表的数据构造是一群具有统一接口界面的对象集合，并可以通过一个对象来访问所有的对象（遍历）。

```cpp
#include <iostream>
#include <vector>
#include <typeinfo> 
using namespace std;

class Component
{
public:
    virtual void operation()=0;
    virtual void add(Component* c){};
    virtual void remove(Component* c){};
    virtual Component* getChild(int i){};
};

class Leaf: public Component
{
public:
    void operation()
    {
        cout<<"Leaf"<<endl;
    };
};

class Composite: public Component
{
public:
    void operation()
    {
        cout<<"Composite"<<endl;
    };
    void add(Component* c)
    {
        mChildren.insert(mChildren.begin(), c);
    };
    void remove(Component* c)
    {        
        vector<Component*>::iterator it;
        for(it = mChildren.begin(); it < mChildren.end(); it++)
            if(*it == c)
            {
                mChildren.erase(it);
                break;
            }                
    };
    Component* getChild(int i)
    {
        if(i < 0 || i >= mChildren.size())
            return NULL;
        return mChildren[i]; 
    };
private:
    vector<Component*> mChildren;
};

void printComponent(Component* pComponent)
{
     pComponent->operation();
     if(!dynamic_cast<Composite*>(pComponent))
         return;     
     int i=0;
     Component* childComponent;
     while(childComponent = pComponent->getChild(i++))
     {
         printComponent(childComponent);
     };
};
int main()
{
    Leaf *pLeaf1 = new Leaf();
    Leaf *pLeaf2 = new Leaf();
    
    Composite* pComposite = new Composite;
    pComposite->add(pLeaf1);
    pComposite->add(pLeaf2);
    Composite* pComposite2 = new Composite;
    pComposite2->add(pComposite);
    printComponent(pComposite2);
    
    system("pause");
    return 0;
}
```