---
layout: post
title: 设计模式[6]-Interpreter
category: Past
description: 最常用场景在于语法分析
---
Type: Behavioral

Interpreter：给定一个语言，定义其语法的含义，同时拦截器利用其含义拦截其中的句子。

```cpp
#include <iostream>  
#include <string>  
#include <vector>  
using namespace std;  
  
class Context  
{  
public:  
    Context(string pInput):mInput(pInput){};
    string mInput;  
};
  
class AbstractExpression  
{  
public:  
    virtual void interpret(Context* contex) =0;  
}; 

class TerminalExpression : public AbstractExpression  
{  
public:  
    void interpret(Context* context)  
    {
        string &s = context->mInput;
        cout<<"TerminalExpression:";
        for(int i=0; i<s.length(); i++){
            if(s[i] == '+' || s[i] == '-'  || s[i] == '*'  || s[i] == '/' )
                cout<<" "<<s[i];  
        }
        cout<<endl;
    }  
};  
class NonterminalExpression : public AbstractExpression  
{  
public:  
    void interpret(Context* context)  
    {  
        cout<<"NonterminalExpression:";
        string &s = context->mInput;
        for(int i=0; i<s.length(); i++){
            if(s[i] == '0' || s[i] == '1' || s[i] == '2'  || s[i] == '3'  
                    || s[i] == '4' || s[i] == '5' || s[i] == '6'  
                    || s[i] == '7' || s[i] == '8' || s[i] == '9' )
                cout<<" "<<s[i];  
        }
        cout<<endl;
    }  
};  

int main()  
{  
    Context* context=new Context("123 + 456 * 789");  
    vector<AbstractExpression*> expressions;  
    expressions.push_back(new TerminalExpression());  
    expressions.push_back(new NonterminalExpression());
    vector<AbstractExpression*>::iterator iter=expressions.begin();  
    while(iter!=expressions.end())  
    {  
        (*iter)->interpret(context);  
        iter++;  
    }  
    system("pause"); 
}
```





