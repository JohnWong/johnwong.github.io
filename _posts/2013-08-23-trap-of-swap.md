---
layout: post
title:  交换两个数不使用临时变量的陷阱
category: Past
description: 这个问题告诉我们有的面试题就真的是面试题，看起来很美但是一般人不这么写。
---

之前看面试书有类似的问题，觉得用异或或者加减这样减少一个临时变量是更精妙的方法。

但是事实上，异或交换，需要先判断两个数是否相等，不然就清零了。在性能上也不一定能更优，参见[http://blog.csdn.net/solstice/article/details/5166912](http://blog.csdn.net/solstice/article/details/5166912)。给代码的维护也带来不必要的麻烦。

加减的方法，可能造成内存溢出。说到底，这种面试题算是偏题吧，考验思维的灵活性，但是没有实际意义。