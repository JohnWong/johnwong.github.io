---
layout: post
title: "java.lang.OutOfMemoryError: PermGen space及其解决方法"
category: past
description: PermGen space的全称是Permanent Generation space，是指内存的永久保存区域。
---

1、
PermGen space的全称是Permanent Generation space,是指内存的永久保存区域OutOfMemoryError: PermGen space从表面上看就是内存益出，解决方法也一定是加大内存。说说为什么会内存益出：这一部分用于存放Class和Meta的信息,Class在被 Load的时候被放入PermGen space区域，它和和存放Instance的Heap区域不同,GC(Garbage Collection)不会在主程序运行期对PermGen space进行清理，所以如果你的APP会LOAD很多CLASS的话,就很可能出现PermGen space错误。这种错误常见在web服务器对JSP进行pre compile的时候。
改正方法：-Xms256m -Xmx256m -XX:MaxNewSize=256m -XX:MaxPermSize=256m

2、
在tomcat中redeploy时出现outofmemory的错误.
可以有以下几个方面的原因:
  1,使用了proxool,因为proxool内部包含了一个老版本的cglib.
  2, log4j,最好不用,只用common-logging
  3, 老版本的cglib,快点更新到最新版。
  4,更新到最新的hibernate3.2

3、
这里以tomcat环境为例，其它WEB服务器如jboss,weblogic等是同一个道理。

一、java.lang.OutOfMemoryError: PermGen space
PermGen space的全称是Permanent Generation space,是指内存的永久保存区域,
这块内存主要是被JVM存放Class和Meta信息的,Class在被Loader时就会被放到PermGen space中,
它和存放类实例(Instance)的Heap区域不同,GC(Garbage Collection)不会在主程序运行期对
PermGen space进行清理，所以如果你的应用中有很多CLASS的话,就很可能出现PermGen space错误,
这种错误常见在web服务器对JSP进行pre compile的时候。如果你的WEB APP下都用了大量的第三方jar, 其大小
超过了jvm默认的大小(4M)那么就会产生此错误信息了。
解决方法： 手动设置MaxPermSize大小
修改TOMCAT_HOME/bin/catalina.sh
在“echo "Using CATALINA_BASE:   $CATALINA_BASE"”上面加入以下行：
JAVA_OPTS="-server -XX:PermSize=64M -XX:MaxPermSize=128m
建议：将相同的第三方jar文件移置到tomcat/shared/lib目录下，这样可以达到减少jar 文档重复占用内存的目的。

二、java.lang.OutOfMemoryError: Java heap space
Heap size 设置
JVM堆的设置是指java程序运行过程中JVM可以调配使用的内存空间的设置.JVM在启动的时候会自动设置Heap size的值，
其初始空间(即-Xms)是物理内存的1/64，最大空间(-Xmx)是物理内存的1/4。可以利用JVM提供的-Xmn -Xms -Xmx等选项可
进行设置。Heap size 的大小是Young Generation 和Tenured Generaion 之和。
提示：在JVM中如果98％的时间是用于GC且可用的Heap size 不足2％的时候将抛出此异常信息。
提示：Heap Size 最大不要超过可用物理内存的80％，一般的要将-Xms和-Xmx选项设置为相同，而-Xmn为1/4的-Xmx值。 
解决方法：手动设置Heap size
修改TOMCAT_HOME/bin/catalina.sh
在“echo "Using CATALINA_BASE:   $CATALINA_BASE"”上面加入以下行：
JAVA_OPTS="-server -Xms800m -Xmx800m   -XX:MaxNewSize=256m"

三、实例，以下给出1G内存环境下java jvm 的参数设置参考：
JAVA_OPTS="-server -Xms800m -Xmx800m  -XX:PermSize=64M -XX:MaxNewSize=256m -XX:MaxPermSize=128m -Djava.awt.headless=true "






































































