---
layout: post
title: 阿里实习面试总结
category: past
description: 这次妥妥的倒在了一面上。还是基础不够扎实。
---

这次妥妥的倒在了一面上。还是基础不够扎实。

#### 1. 重载与多态区别
重载（overload）一般是用于在一个类内实现若干重载的方法，这些方法的名称相同而参数形式不同。
重载的规则：
a、在使用重载时只能通过相同的方法名、不同的参数形式实现。不同的参数类型可以是不同的参数类型，不同的参数个数，不同的参数顺序（参数类型必须不一样）；
b、不能通过访问权限、返回类型、抛出的异常进行重载；
c、方法的异常类型和数目不会对重载造成影响；

重写/覆盖（override），子类在继承父类时，重写父类中的方法。
重写的规则：
a、重写方法的参数列表必须完全与被重写的方法的相同,否则不能称其为重写而是重载.
b、重写方法的访问修饰符一定要大于被重写方法的访问修饰符（public>protected>default>private）。
c、重写的方法的返回值必须和被重写的方法的返回一致；
d、重写的方法所抛出的异常必须和被重写方法的所抛出的异常一致，或者是其子类；
e、被重写的方法不能为private，否则在其子类中只是新定义了一个方法，并没有对其进行重写。
f、静态方法不能被重写为非静态的方法（会编译出错）。

多态为了避免在父类里大量重载引起代码臃肿且难于维护。通过重写实现。

```java
public class Shape {  
    public static void main(String[] args) {  
        Triangle tri = new Triangle();  
        System.out.println("Triangle is a type of shape? " + tri.isShape());// 继承  
        Shape shape = new Triangle();  
        System.out.println("My shape has " + shape.getSides() + " sides."); // 多态  
        Rectangle Rec = new Rectangle();  
        Shape shape2 = Rec;  
        System.out.println("My shape has " + shape2.getSides(Rec) + " sides."); // 重载  
    }  
  
    public boolean isShape() {  
        return true;  
    }  
  
    public int getSides() {  
        return 0;  
    }  
  
    public int getSides(Triangle tri) { // 重载  
        return 3;  
    }  
  
    public int getSides(Rectangle rec) { // 重载  
        return 4;  
    }  
}  
  
class Triangle extends Shape {  
    public int getSides() { // 重写,实现多态  
        return 3;  
    }  
}  
  
class Rectangle extends Shape {  
    public int getSides() { // 重写,实现多态  
        return 4;  
    }  
}
```

#### 2. read()执行时操作系统完成的工作

#### 3. 进程有哪些状态

基本状态：运行-就绪-阻塞（也称为等待或睡眠）。实际的系统中经常引入新建态和终止态。有的系统引入了挂起态。
Java线程状态共6个：NEW、RUNNABLE、BLOCKED、WAITING、TIMED_WAITING、TERMINATED

#### 4. url中参数去掉一部分的算法

当时想到了切分字符串和正则替换，但是写的正则有问题。面试结束和面试官交流，他提示扫描一遍就可以。

```java
package monitor;  
  
import java.util.Arrays;  
  
class CheckHelper {  
    private char temp[] = new char[64];  
    private String params[];  
    private boolean check[];  
    private int tag = 0;  
  
    public CheckHelper(String params[]) {  
        this.params = params;  
        check = new boolean[params.length];  
    }  
  
    public void initCheck() {  
        for (int i = 0; i < check.length; i++)  
            check[i] = true;  
        tag = 0;  
    }  
  
    public void doCheck(char c) {  
        for (int i = 0; i < params.length; i++) {  
            String param = params[i];  
            temp[tag] = c;  
            if (tag >= param.length() || param.charAt(tag) != c) {  
                check[i] = false;  
            }  
        }  
        tag++;  
    }  
  
    public String getResult() {  
        for (int i = 0; i < params.length; i++) {  
            String param = params[i];  
            if (check[i] && param.length() == tag) {  
                initCheck();  
                return null;  
            }  
        }  
        String ret = new String(Arrays.copyOf(temp, tag));  
        initCheck();  
        return ret;  
    }  
}  
  
public class Test {  
    public static String removeParam(String url, String[] params) {  
        CheckHelper ch = new CheckHelper(params);  
        ch.initCheck();  
        StringBuilder sb = new StringBuilder();  
        boolean start = false;  
        boolean rest = false;  
        boolean copy = false;  
        for (int i = 0; i < url.length(); i++) {  
            char c = url.charAt(i);  
            if (!start) {  
                sb.append(c);  
                if (c == '?')  
                    start = true;  
            } else if (c == '=') {  
                rest = true;  
                String ret = ch.getResult();  
                if (ret != null) {  
                    if (sb.charAt(sb.length() - 1) != '?')  
                        sb.append('&');  
                    sb.append(ret);  
                    sb.append('=');  
                    copy = true;  
                } else {  
                    copy = false;  
                }  
            } else if (!rest) {  
                ch.doCheck(c);  
            } else if (c != '&') {  
                if (copy)  
                    sb.append(c);  
            } else {  
                ch.initCheck();  
                rest = false;  
                copy = false;  
            }  
        }  
        return sb.toString();  
    }  
  
    public static void main(String[] args) throws Exception {  
        String url = "http://s.taobao.com/search?spm=a230r.1.0.100.S98nmj&" +  
                "q=Apple%2F%C6%BB%B9%FB+MacBook+Pro+MD101CH%2FA&v=product&p=" +  
                "detail&pspuid=202666380&cat=1101&from_pos=55_1101.xlcombo_1_2_202666380";  
        String[] params = { "spm", "pspuid", "cat" };  
        System.out.println(removeParam(url, params));  
    }  
}
```

PS. 2014年的今天已经是阿里巴巴的一员了。觉得应该对自己的Java有信心并提出让Java工程师来面试我。