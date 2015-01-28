---
layout: post
title: 设计模式[14]-Composite
category: Past
description: 将对象组合成树形结构以表示“部分-整体”的层次结构。
---
Type: Structural

Composite: 将对象组合成树形结构以表示“部分-整体”的层次结构。Composite使得用户对单个对象和组合对象的使用具有一致性。

有时候又叫做部分-整体模式，它使我们树型结构的问题中，模糊了简单元素和复杂元素的概念，客户程序可以向处理简单元素一样来处理复杂元素,从而使得客户程序与复杂元素的内部结构解耦。