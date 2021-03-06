---
layout: post
title: "Scala程序设计读书笔记[6:10]"
category: past
description: Programming Scala
---
### 第六章 函数值和闭包
1. 高阶函数  以其它函数为参数的函数。

2. 函数值  可以在函数里创建函数，将函数赋给引用。函数参数中例如codeBlock: Int => Int。函数值包含多行代码或者作为参数传入时有多个参数，需要用圆括号包起来。

3. 具有多参数值的函数值 具有多个参数的函数值例如operation: (Int, Int) => Int)。想要遍历容器中元素，执行一些操作可以使用foldLeft方法，即/:。使用方法，0为初值：array.foldLeft(0){}，(0 /: array){}。尖括号中为两参数函数值如(a, b) => a+b。

4. Curry化 curry化可以把函数从接收多个参数变成接收多个参数列表。用一组实参多次调用同一个函数的时候能够用curry化来减少噪音？定义时每组参数用括号包起来。调用时可以用个括号或者尖括号。但是第一个参数列表必须使用括号。非第一个参数列表只能一个参数。

5. 重用函数值 将函数值赋给var或者val可以。重用函数值而不是参数列表。似乎必须指明返回类型例如：{ input : Int => input }

6. 参数位置记法  如果某个参数在函数里只使用一次，就可以下划线可以表示。(a, b) => Math.max(a, b)可以协作Math.max(_, _)。也可以表示整个参数列表，协作Math.max _。如果只是传给下层甚至协作Math.max。

7. Execute Around Method  假设有个类需要自动开启事务，在用完对象之后需要显示的结束事务。正确启动事务可以依赖于构造函数，终结部分有些棘手，可以用Execute Around Method。利用私有类和伴生类。伴生类的一个方法接收函数值作为参数，创建私有类的实例，在try和finally块的保护下把实例传给传入的函数值。调用的时候传入代码块，就能按照代码块执行资源的操作，并确保调用finally中的清除方法。

8. Loan Pattern  上个模式的变体。在方法有函数值参数，方法内创建资源，并在try和finally的保护下将资源传给函数值，finally中做资源释放。调用时传入代码块。代码块中可以得到资源的实例。代码块执行完毕后会释放资源。

9. 偏应用函数  偏应用函数相对全应用函数，只接收部分参数，将未接收的参数绑定到全应用函数上。val logWithDateBound = log(new Date, _ : String)。

10. 闭包  闭包是可以包含自由（未绑定到特定对象）变量的代码块；这些变量不是在这个代码块内或者任何全局上下文中定义的，而是在定义代码块的环境中定义。在Scala中传入的代码块中可以使用定义代码块环境中的变量。

### 第七章 Trait和类型转换
1. Trait  指的是可以混入或者融入一个类层次结构的行为。就像一个拥有部分实现的接口，提供了一个介于单一继承和多重继承的中间地带。trait里定义和初始化的val和var会混入trait的类内部得以实现。定义过而未被初始化的val和var则认为是抽象的，需要由混入这些trait的类实现。如果类不继承其他类，可以用extends关键字混入trait。用关键字with可以混入更多的trait。一个类混入trait后，通过它的实例可以调用trait的方法，也可以把它当作trait的引用。与类的区别：a)需要混入类去实现已声明而未初始化的变量和值；b)其构造器不能有任何参数。trait会编译为Java的接口，还有对应的实现类，里面包含了trait实现的方法。k

2. 选择性混入  还可以再实例一级对trait进行选择性混入，就可以把特定的类的实例当作trait，使用with。new Cat with Friend。

3. trait用于装饰模式  trait可用于装饰对象，使其具有一些能力。class Check有check方法。定义trait CreditCheck和EmploymentCheck继承Check，复写其check方法，最后调用super.check。这样new Check with CreditCheck with EmploymentCheck check将会依次调用EmploymentCheck、CreditCheck和Check的check方法，给Check的check方法增添了额外的功能。

4. Trait方法的延迟绑定  如果Check的check方法未实现，则Check必须为abstract，同时继承Check的trait也必须将check标为abstract，无论其有没有实现。

5. 隐式类型转换  将方法标记为implicit，只要它在当前范围存在（通过import可见或者位于当前文件），scala就会自动调用。方法名格式为convertInt2DateHelper。scala一次至多应用一个隐式转换。

### 第八章 使用容器
1. 常见Scala容器  List/Set/Map。scala虽然提供了可变容器和不可变容器，但是如果想修改容器而且对容器的所有操作都在一个线程里，可以选择可变容器。如果计划跨线程或者跨actor使用容器，不变容器更好。不仅线程安全，而且没有副作用。可选包为scala.collection.mutable或scala.collection.immutable。不必用新建，可以用Set(1, 2)来创建，scala会调用apply方法，也成工厂方法。容器类型不必指定，得到的是Set[Int]。

2. 使用Set  调用filter方法找到包含指定字符的set子集：feeds filter ( _ contains "blogspot")。set使用指定间隔符转string：mkString(", ")。+方法添加元素，返回的是新容器。++可以合并两个set。**求交集。map方法对每个元素应用传入的函数值，返回结果的数组。toArray转为数组。数组可以apply方法（apply可以省略）取得元素。书中set.toArray(0)的写法编译错误，需要一个引用p指向数组，之后p(0)返回第一个元素。

3. 使用Map  Map(1->2, 2->3)。filterKeys根据键过滤，filter根据键值对过滤。get根据值返回键，返回的是Option。apply方法返回值，不存在则抛出异常。update方法现在变为updated，修改键对应的值，不存在则添加键值，返回新map。

4. 使用List  List只有不变的实现。head访问第一个元素，tail访问最后一个元素。可以用apply方法访问指定索引的值。在前面添加元素可以用1::a，合并List a:::b。filter可以筛选，forall可以检查是否都符合条件，exists判断是否有满足条件的元素。还有方法map、foldLeft、foldRight。foldRight类似，但是从又开始计算。

5. 方法命名约定  :提升流畅性，:在后表示调用目标是运算符后面的实例，例如::。同样调用目标是后面的还有一元运算符+、-、!、~。+映射为unary_+，其他三个也一样。

6. for表达式  foreach提供了内部迭代器，不必控制循环。控制循环需要用for。for表达式接收的参数包括一个或多个生成器，0或多个定义，还有0或多个过滤器，分号分隔。yield关键字可选，表示返回一个多值容器，而不是一个Unit。也可以用map实现循环控制(1 to 10).map()。添加过滤器：for(i <- 1 to 10; if i % 2 == 0) yield i * 2。也可以将分号替换为换行符，括号改写为尖括号。生成器里可以定义变量，每个迭代里都会以这个名字定义一个新的val。如果for表达式里提供了多个生成器，则每个生成器都会形成一个内部循环。最右的生成器控制这最内的循环。

### 第九章 模式匹配和正则表达式
1. 匹配字面量和常量  match是一个对Any起作用的表达式。它会对目标执行模式匹配，传入的代码块使用case表达式。匹配通配符  case后使用_可以代替default。

2. 也可以匹配元组和列表  数组对于不关心的元素，可以用_省略，多个可以用_*。如果需要引用余下的项可以用在通配符前加变量名和@。

3. 类型和卫戍句的匹配  case msg: Int => ...也可以case msg: Int if (msg > 100) 这样匹配类型和值。

4. case表达式里的模式变量和常量  模式变量以小写字母开头，常量以大写字母开头。如果在当前作用域内有一个有着与模式变量同样名字的字段将会报错。这时占位符需要显示指定作用域，如this.xx或者伴生对象Object.xx。

5. 使用case类进行模式匹配  case类对case进行了一定程度的封装。定义abstract case class，并定义一些cass class继承刚才的类。首先匹配case class是否相同，然后再匹配case class的参数是否符合。如果定义为sealed abstract cass class，就告诉scala除了这个文件中的case class的子类，不会有其他子类，这样如果定义了case class的子类但是匹配的时候没有出现，就会报编译错误。如果定义的case class没有参数，记得用的时候记得加括号。不然传入的是伴生对象。这个伴生对象混入了scala.Function0 trait，以为这传入的是一个函数，而不是对象。

6. 使用提取器进行匹配  定义包含unapply方法的object，返回Boolean或者Option。如果返回false或者None则不匹配。

7. 正则表达式   RichString的r方法返回Regex实例。可以使用"""来避免使用转义。
8. 正则表达式当作提取器  val MatchStock = """^(.+):(\d*\.\d+)""".r  ...   case MatchStock("GooG", price) => println(...)

### 第十章 并发编程
1. 促进不变性  使用可变对象写出线程安全代码极端困难，不变对象从根源上解决了这个问题。Scala的并发模型依赖不变性，希望我们把不变对象当作消息在actor间传递。不变性优势有：
  a) 天生线程安全，无法修改状态
  b) 没有复杂的状态转换，简单易用
  c) 可以在应用间共享和重用。
  d) 不易出错，因为不会随意改变对象状态。

2. 使用Actor并发  actor提供了一种基于事件的轻量级线程。使用scala.actors.Actor伴生对象的actor()方法，就可以创建一个actor。它接受一个函数值/闭包做参数，一创建好就开始运行。用!()方法给actor发消息，receive方法从actor接收消息，通过case取回消息。receive也可以闭包为参数，通常用模式匹配处理接收到的消息。

3. 消息传递  发送不阻塞，接收不中断。在actor调用receive方法接收之前，消息一直等在那里。mailboxSize是receive方法中的隐含参数，消息的数量。同步发送和接收消息使用!?()方法。不过可能引起潜在死锁。

4. Actor类  之前使用Actor单例对象的actor方法，大多数情况下够用。如果想在actor启动时进行显式控制，希望在actor里存入更信息，可以创建一个对象，混入Actor trait。调用start()方法会有单独线程处理actor的act方法。exit()方法可以中止线程执行。

5. actor方法  用actor()方法创建一个匿名的actor。actor会在另外线程中执行。与actor交互的顺序是没有保证的。actor对消息的接收和处理没有预先强加的顺序。

6. receive和receiveWithin方法  receive接收一个函数值/闭包，返回一个处理消息的应答，会造成阻塞。receiveWithin接收一个timeout参数，其中case可以为TIMEOUT，用于超时时的处理。

7. react和reactWithin方法  receive和receiveWithin方法的actor具有线程关联性；他们会持续使用分配给他们的同一个线程。react和reactWithin的actor不具有线程关联性，可以自由的交换彼此的线程，可以由任何可用的线程处理。鼓励使用react代替receive。副作用是在处理消息的末尾调用适当方法，否则actor不再处理任何消息。loop和loopWhile是更好的处理方法。

8. loop和loopWhile

9. 控制线程执行  shiyong receive时每个actor运行在自己的线程里，react让actor共享来自线程池的线程。SingleThreadedSchedule可以让Scala在主线程里运行actor。Scheduler.impl = new SingleThreadedScheduler 可以使主线程里运行actor。想要使某个actor在一个线程中运行，需要类继承Actor，覆写scheduler方法，返回SingleThreadedScheduler的实例。

10. 在各种接收方法中选择  应该使用within的方法，以便在一段时间没有收到响应式恢复过来。如果想要在一个工作流执行中间从另一个actor接受消息，那么receiveWithin很合适，actor会一直阻塞知道收到消息，不过actor不能太多，因为每一个在结束之前都会持有一个线程。另一方面如果想要实现一个服务接收消息，快速响应调用者，应该使用reactWithin，在等待消息到来期间不会持有线程。如果不确定用哪一个，在reactWithin不能满足需求时再使用receiveWithin。记住要在loopWhile里调用reactWithin，以便actor可以持续处理更多消息。如果更倾向于函数式风格，也可以在reactWithin里递归调用方法。如果reactWithin里只有一两个case语句，后一种方法也可以。
