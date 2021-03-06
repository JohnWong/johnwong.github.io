---
layout: post
title: "Scala程序设计读书笔记[11:14]"
category: past
description: Programming Scala
---
### 第十一章 与Java互操作
1. 在Scala里使用Scala类  如果在脚本中使用，不需编译被引用的Scala类。如果在编译过的Scala或Java代码中使用就需要编译。指定代码目录为entities和当前目录：`scala -sourcepath entities:. userPerson.scala`。编译引用类： `scalac -d . -classpath LocationOfPersonClassFile usePersonClass.scala`。用java运行时只要指定scala-library.jar即可：`java -classpath path/scala-library.jar:. UsePersonClass`。

2. 在Scala里使用Java类  如果Java类是标准JDK的一部分，直接用。如果不在java.lang里，就要导入类的包。如果Java类是自己创建的或者第三方，需要用classpath指向字节码位置。如果Java代码有方法或者字段的名字和Scala的关键字冲突，在scala中将冲突的变量/方法放到反引号里。

3. 在Java里使用Scala类  运行时需要将scala-library.jar加入classpath。Scala默认不遵守JavaBean约定，要用@scala.reflect.BeanProperty这个注解生成符合JavaBean约定的getter和setter。如果Scala类有方法由接收闭包，在Java里就不可用。Scala不支持interface关键字，如果想创建接口就创建一个没有实现的trait。Scala将对象（单例对象或伴生对象）编译成一个单例类，类末尾名字有一个$符。单例类会同时创建一个普通类，把调用传给单例类，类名直接访问，例如Buddy.greet()。如果对象是同名类的伴生对象，Scala会创建两个类，一个表示Scala类，另一个表示伴生对象，末尾加$。访问伴生对象需要使用符号MODULE$，如Buddy$.MODULE$.greet()。

4. 继承类  Scala类和Java类可以互相继承。如果方法接受闭包为参数，重写起来有些麻烦。异常也是个问题。Scala没有throws语句，任何方法可以抛出异常，无需显式声明成方法签名的一部分。如果在Java中重写这样的类，在Scala中方法定义前加注解@throws(classOf[NoFlyException]) def fly();。Scala支持注解但是不提供创建注解的语法。如果想创建注解就不得不用Java类做。@throws是已经提供好的注解。

### 第十二章 用Scala做单元测试
1. 使用JUnit  用Scala写好测试后编译成字节码，然后运行测试。编译运行时将JUnit的jar加入classpath。

2. 使用ScalaTest  有着精炼的语法和函数式风格，既可以测试Scala代码，也可以测试Java代码。地址[http://www.artima.com/scalatest](http://www.artima.com/scalatest)

3. 以Canary测试开始  创建类继承org.scalatest.Suite，之后创建该类实例并执行execute方法。

4. 使用Runner  用来测试多个套件。`scala -classpath $SCALATEST:. org.scalatest.tools.Runner -p .`，p指定查找套件的路径。-o可以重定向输出到标准输出而不是GUI，-f重定向到文件。

5. Asserts  ScalaTest提供了===操作符，与assert()方法相比可以打印出更多信息。可以传入第二个参数，传入更多消息。如果检查两个值相等，使用expect，接收一个期望值，一个可选的消息，一个闭包。比较闭包里表达式执行结果与期望值是否相等。

6. 异常测试  异常测试确保被测试的代码单元可以抛出预期的异常。使用try-catch-finally，但是catch中使用的是模式匹配语法。try最后放入fail方法，这样不抛出异常或者抛出未被捕获的异常都会失败。简洁一些可以写成intercept(classOf[IndexOutOfBoundsException], ""){list.get(0)}。接收一个异常类作为参数，一个可选的错误消息，一个闭包。

7. 在测试间共享代码  用BeforeAndAfter trait共享代码。提供了beforeEach和afterEach方法，类似setUp和tearDown方法。还提供了beforeAll和afterAll方法。用闭包共享代码。应用6.7节Execute Around Methond模式，定义一个withList方法，传入函数。方法体内定义List，在try-finally块中传给函数执行，在finally中做一些执行后的任务。可以在多个测试的方法中调用withList，传入要做的测试。

8. FunSuite的函数式风格  继承FunSuite，不再写测试方法，而是调用一个名叫test()的方法，给它提供一个有意义的测试名字和一个闭包，闭包中是测试的主体。

9. 用JUnit运行ScalaTest  让测试套件继承JUnit3Suite，在main方法中junit.textui.TestRunner.run(classOf[UsingJUnit3Suite])。这样能用Scala和JUnit来运行ScalaTest写的测试，不存在JUnit(或TestNG)与ScalaTest之间二选一的问题。

### 第十三章 异常处理
1. 异常处理  可以像Java一样抛出异常throw new WhatEverException，使用try-catch-finally。catch语句中使用case模式匹配来处理异常。

2. 注意catch顺序  如果放了多个catch块，Java会监控他们的顺序。Java中后面Exception执行不到会得到编译错误，scala中不会给出警告，因此使用多个catch块时，必须确保异常由预期的catch块处理。

### 第十四章 使用Scala
1. 获取用户输入  Console.readLine

2. 读写文件  写文件：val writer = new PrintWriter(new File("a.txt"))   writer write "abc"   writer.close()。读文件：import scala.io.Source  Source.fromFile("a.txt").foreach{print}。如果需要一次读一行，就用getLines方法。fromURL方法接收java.net.URL对象，从网络读取数据。getLine方法返回指定行，以1为起始索引。

3. XML作为一等公民  Scala中可以将xml文档之间放入代码就像int或Double一样。 `val xml = <symbols><symbol>a</symbol></symbols>`。类似XPath的查询提取方法xml \ "symbol"，查找其直接后代，传入的字符串@起始，则查找属性。如果要从目标元素出发，搜出层次结构里所有元素，就要用\\方法。text方法获取元素里的文本节点。可以使用模式匹配来提取xml中的信息

4. 读写XML  `import scala.xml.*  XML.load("stocks.xml")。XML.save("stocks2.xml", xml)`

5. GUI  scala.swing.SimjpleGUIApplication，实现top方法，返回一个Frame。目前deprecated Since version 2.8.0 Use SimpleSwingApplication instead。可以使用JavaFX2 (and ScalaFX, which provides a nice Scala API for JavaFX2)

Finished! 不过看完书离熟悉还有很大差距
