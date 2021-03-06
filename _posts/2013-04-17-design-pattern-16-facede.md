---
layout: post
title: 设计模式[16]-Facede
category: past
description: 典型应用是数据库JDBC的应用。
---

Type: Structural

Facade: 为子系统中的一组接口提供一个一致的界面。典型应用是数据库JDBC的应用。
Jsp中常用的操作数据库的方法如下：

```java
public class DBCompare {  
　　Connection conn = null;  
　　PreparedStatement prep = null;  
　　ResultSet rset = null;   
　　try {  
　　 　　Class.forName( "<driver>" ).newInstance();  
　　　　 conn = DriverManager.getConnection( "<database>" );  
　　　　  
　　　　 String sql = "SELECT * FROM <table> WHERE <column name> = ?";  
　　　　 prep = conn.prepareStatement( sql );  
　　　　 prep.setString( 1, "<column value>" );  
　　　　 rset = prep.executeQuery();  
　　　　 if( rset.next() ) {  
　　　　　　　　System.out.println( rset.getString( "<column name" ) );  
　　　　　}  
　　} catch( SException e ) {  
　　　　 e.printStackTrace();  
　　} finally {  
　　　　 rset.close();  
　　　　 prep.close();  
　　　　 conn.close();  
　　}  
} 
```

在应用中,经常需要对数据库操作,每次都写上述一段代码肯定比较麻烦,需要将其中不变的部分提炼出来,做成一个接口,这就引入了facade外观对象.如果以后我们更换Class.forName中的`<driver>`也非常方便,比如从Mysql数据库换到Oracle数据库,只要更换facade接口中的driver就可以。

```java
public class DBCompare {  
  
　 String sql = "SELECT * FROM <table> WHERE <column name> = ?";　　  
  
　　try {  
　　 　　Mysql msql=new mysql(sql);  
　　　　 msql.setString( 1, "<column value>" );  
　　　　 rset = msql.executeQuery();  
　　　　 if( rset.next() ) {  
　　　　　　　　System.out.println( rset.getString( "<column name" ) );  
　　　　　}  
　　} catch( SException e ) {  
　　　　 e.printStackTrace();  
　　} finally {  
　　　　 mysql.close();  
　　　　 mysql=null;  
　　}  
}
```

参考自[解道网](http://www.jdon.com/designpatterns/designpattern_Facade.htm)
还是看着Java代码亲切。。。