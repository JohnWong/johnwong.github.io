---
layout: post
title: 设计模式[2]-Chain of Responsibility
category: Past
description: 响应链最常用的场景就是界面上对点击等的处理
---
Type: Behavioral

```CPP
#include <iostream>  
using namespace std;  
typedef int Request;  
  
class Handler  
{  
public:  
    Handler(Handler *pSuccessor = NULL):m_pSuccessor(pSuccessor){};  
    // 纯虚函数,由派生类实现  
    virtual void handleRequest(Request request) = 0;  
  
protected:  
    Handler* m_pSuccessor;  
};  
  
class ConcreateHandler1: public Handler  
{  
public:      
    void handleRequest(Request request)  
    {  
        if(request > 0)  
        {  
            cout<<"ConcreateHandler1 handle request."<<endl;  
        } else {  
            if(m_pSuccessor != NULL){  
                m_pSuccessor->handleRequest(request);  
            }  
        }  
          
    }  
};  
  
class ConcreateHandler2: public Handler  
{  
public:  
    ConcreateHandler2(Handler *pSuccessor = NULL){  
        m_pSuccessor = pSuccessor;  
    }  
    void handleRequest(Request request)  
    {  
        if(request > 10)  
        {  
            cout<<"ConcreateHandler2 handle request."<<endl;  
        } else {  
            if(m_pSuccessor != NULL){  
                m_pSuccessor->handleRequest(request);  
            }  
        }  
          
    }  
};  
  
int main()  
{  
    Handler *p1 = new ConcreateHandler1();  
    Handler *p2 = new ConcreateHandler2(p1);  
    Request request = 1;  
    p2->handleRequest(request);  
    request = 12;  
    p2->handleRequest(request);  
    system("pause");  
    return 0;  
}
```