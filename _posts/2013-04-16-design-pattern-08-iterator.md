---
layout: post
title: 设计模式[8]-Iterator
category: past
description: 在Java容器类中常用的迭代器。
---

Type: Behavioral

Iterator：提供一个方法连续访问一个聚合对象的元素，同时不暴露其底层表示

``` c++
#include <iostream>  
using namespace std;  
#define Data int  
class Iterator  
{  
public:  
    virtual Data* next()=0;  
};  
  
class ConcreteIterator: public Iterator  
{  
public:  
    ConcreteIterator(Data* data, int* size)  
    {  
        m_pData = data;  
        m_pSize = size;  
        mIndex = 0;  
    };  
    Data* next()  
    {  
        if(m_pData != NULL && mIndex < *m_pSize){  
            return &m_pData[mIndex++];  
        } else {  
            return NULL;  
        }  
    };     
private:  
    int mIndex;  
    Data* m_pData;  
    int* m_pSize;  
};  
  
class Aggregate  
{  
public:  
    virtual Iterator* createIterator() = 0;  
};  
  
class ConcreteAggregate: public Aggregate  
{  
public:  
    ConcreteAggregate(int size)  
    {  
        mSize = size;  
        mData = new Data[size];  
        for(int i=0;i<size; i++)  
            mData[i] = i;  
    };  
    Iterator* createIterator()  
    {  
        Iterator* iterator = new ConcreteIterator(this->mData, &this->mSize);  
        return iterator;  
    };  
private:  
    Data* mData;  
    int mSize;  
};  
  
int main()  
{  
    Aggregate* pAggregate = new ConcreteAggregate(4);  
    Iterator*  pIterator  = pAggregate->createIterator();  
  
    Data* data;  
    int count = 0;  
    while (data = pIterator->next())  
    {  
        if(count ++ > 10)  
            break;  
        cout <<*data<<endl;  
    }  
    system("pause");  
    return 0;  
}
```