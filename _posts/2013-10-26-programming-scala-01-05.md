---
layout: post
title: "Scala程序设计读书笔记[1:5]"
category: past
description: Programming Scala
---
## Scala程序设计: Java虚拟机多核编程实战

一直好奇什么样的语言能够不需要加锁解决线程同步问题，能够解决Twitter的性能问题，想了解什么是函数式编程。于是找工作的间隙看了这本书，扩展一下视野。

Source Code: [http://media.pragprog.com/titles/vsscala/code/vsscala-code.zip](http://media.pragprog.com/titles/vsscala/code/vsscala-code.zip)

Scala Online Editor：

URL: [http://www.scala-tour.com/#/expression-and-values](http://www.scala-tour.com/#/expression-and-values)  
API: [http://www.scala-tour.com/run?code=println(%22abc%22)](http://www.scala-tour.com/run?code=println(%22abc%22))


### 第一章 简介
Scala混合了函数式和面向对象。用Scala创建多线程应用的时候，你会倾向于函数式编程风格，用不变状态编写无锁代码。Scala提供了一个基于actor的消息传递模型，消除了并发的数据竞争和加锁问题。

在函数式编程中，和ErLang相比的优势：a) 强类型，b) 运行与JVM，可以与Java互操作。

与JVM其他语言Groovy、JRuby和Clojure相比，优势是：能通同时提供函数式风格和良好并发支持的强类型语言。

Scala特性：

* 基于事件的并发模型
* 既支持命令式风格，也支持函数式风格
* 纯面向对象的
* 与Java混合
* 强制使用自适应静态类型
* 简洁而又表现力
* 构建于一个微内核之上
* 高度可扩展，用更少代码创建高性能应用

### 第二章 起步

下载地址：[http://www.scala-lang.org](http://www.scala-lang.org)
脚本运行建议sublime text+自定义build system。
编译scala可以使用IDE+插件[http://www.scala-lang.org/old/node/91](http://www.scala-lang.org/old/node/91)

### 第三章 Scala步入正轨

1. val相对var初始化后不可改变变量指向其他引用

2. 点和括号是可选的

3. Scala把一切视作对象

4. 元组和多重赋值

5. 三引号的多行字符串以及前导符“|”

6. 自适应默认做法：  
  a) 支持脚本  
  b) return可选，自动返回最后的求值表达式。如果使用return需要显式提供方法返回类型  
  c) 分号半可选，可能产生歧义的时候需要加  
  d) 类和方法默认public，不必显示写  
  e) 轻量级JavaBean创建  
  f) 不强制捕获不关心的异常

7. 默认导入包：
  java.lang：常用java类型；
  scala：Scala类型；
  scalaPredef：类型，隐式转换及常用方法

8. 运算符重载，实际没有运算符，是方法名省略了点和括号的方法。

9. 复制结果是Unit，因此a=b=c在scala中不存在

10. ==基于值比较，继承字Any类，为final。特定实现需要改写equals方法。基于引用比较需要使用eq方法。

11. 细粒度访问控制，private和protected可以加访问控制，this或者包名

### 第四章 Scala的类

1. 定义字段、方法和构造函数
Scala把主构造函数放到了类定义中。参数中的val转换成private final字段，并创建同名public取值方法。声明为var的定义为private，并创建public取值和赋值方法。都不是的话创建private字段和private的getter和setter。放到类定义中的任何表达式或者可执行语句都作为主函数的一部分。定义变量时_代表使用默认值。

2. 类继承重写方法需要override关键字。副构造函数可以通过定义this方法实现。副构造函数第一条语句要么调用主构造函数，要么调用副构造函数。只有主构造函数才能往基类构造函数中传参数。

3. 单例对象
使用object创建，不能给其主构造函数传递参数。

4. 伴生对象
创建一个object和类同名，就是伴生对象。类和伴生对象之间没有界限，可以互相访问private内容。把类的构造函数标记为private就可以实现单例对象。
5. static  scala没有静态字段和静态方法，通过伴生对象支持类一级的操作。伴生对象加括号调用其apply方法。

### 第五章 自适应类型
1. 静态类型  又称成编译时类型检查。scala根据定义或赋值推演类型，如果将其他类型赋给将会编译错误。

2. Scala中特殊类型：Any、Nothing和Option

3. import语句里的下划线相当于java中的星号。如果加在类名后相当于static import。默认引入当前目录。被引用的scala文件需要先scalac编译。

4. 容器和类型推演  不带类型的容器实际传入了Nothing。因此带类型容器不能赋给不带类型容器的引用。也不能赋给Any类型的容器。只有容器类型相同才能赋给。

5. Any类型  是所有Scala类型的超类，抽象类。方法由!=, =, asInstanceOf, equals, hashCode, isInstanceOf, toString。直接后代是AnyVal和AnyRef。AnyRef包含了Java的Object方法，如notify，wait，finalize。

6. Nothing类型  所有类型的子类，实例不会存在，作用是帮助类型推演更加平滑。

7. Option类型  Some[T]和None都继承自Option[T]。其getOrElse方法可以得到值，如果不存在，得到传入的参数。

8. 方法返回类型推演  使用等号定义方法启用方法返回类型推演。

9. 传递变参  如果方法接受参数需要指定参数名字及类型。末尾参数可以接受可变数目的实参，在类型信息后使用星号。但是不能传入数组。如果想将数组展开成离散值，可以用:_*

10. Scala不支持协变和你变。子类实例容器赋给基类容器能力称为协变，超类实例容器赋给子类容器的能力称为逆变。

11. 参数化类型的可变性  通过特殊语法实现子类数组当作父类数组：playWithPets\[T <: Pet](pets: Array[T])。也可以将数组的参数化类型限定为源数组参数化类型的超类：copyPets\[S, D >: S](fromPets: Array[S], toPets: Array[D])。可以把派生类容器当作基类的容器，实现协变：MyList[+T]；也可以用-T实现逆变。
