---
layout: post
title: "FineReport简明教程"
category: past
description: 帆爷让帮忙研究一下FineReport，可能在项目中使用。
---
软件安装及帮助

1. 软件下载地址：http://www.finereport.com/products/trial

2. 注册及获取激活码：http://www.finereport.com/products/login需要手机接收验证码或者致电获取。注册成功后收到邮件包含用户名密码及激活码。

3. 帮助系统：http://www.finereporthelp.com/或者安装后帮助->学习教程

4. 第一次安装后打开软件需要填入获取的验证码。试用版本禁用了一些功能，限制了最大连接数。

5. 系统演示。帮助->演示

可以配置的管理员用户名和密码，这些信息保存在：

%安装目录%\WebReport\WEB-INF\resources\privilege.xml

定义数据连接
打开模版设计器软件 服务器->定义数据连接

支持JDBC和JNDI，JDBC包括Oracle、Mysql、DB2、SQLServer、Sybase、Access等只需填写URL和用户名密码即可。数据连接保存在：

%安装目录%\WebReport\WEB-INF\resources\datasource.xml

设计报表
打开模版设计器软件 新建工作簿，在数据集面板新建数据库查询，将查询到的字段拖拽到工作簿中，添加表头等即可。我们设计了报表GoodsList.cpt。默认设计好的报表保存目录是：

%安装目录%\WebReport\WEB-INF\reportlets。

部署
可以选择独立部署或者嵌入式部署。由于是集成到已有项目中，因此选择嵌入式部署。

1. 将%FineReport_HOME%\WebReport\WEB-INF目录下面的classes,lib,reportlets,resources四个目录复制到%项目目录%\WEB-INF下。

2. 整合web.xml文件

tomcat集成只需要在已有工程的web.xml中添加相应的servlet与servlet-mapping子元素。

将%FineReport_HOME%/WebReport/WEB-INF下的web.xml中如下的部分复制到 %项目目录%/WEB-INF下的web.xml中，在最后一个servlet之后插入：

```xml
<servlet>  
    <servlet-name>ReportServer</servlet-name>  
    <servlet-class>com.fr.web.ReportServlet</servlet-class>  
    <load-on-startup>0</load-on-startup>  
</servlet>  
<servlet-mapping>  
    <servlet-name>ReportServer</servlet-name>  
    <url-pattern>/ReportServer</url-pattern>  
</servlet-mapping>  
```

3. 检测是否部署成功

重新启动Tomcat， 启动浏览器，在地址栏输入

http:/ip:服务器端口号/项目所在目录/ReportServer，能成功进入管理平台，则表明FineReport应用部署Tomcat服务器成功。

ReportServer?op=fs是数据决策系统

ReportServer?op=fr_platform是FR管理平台，这里可以设置管理员账号以及自定义身份验证。

Web页面集成
FineRepor报表可以通过Frame框架直接集成到Web页面中，Web页面可以有很多种脚本语言写的，比如Jsp、Asp、PHP、VB、JavaScript、Html 等，可以将报表嵌入在Frame框架内从而显示在Web页面中。

若您希望自己系统页面中的按钮调用FineReport内部现成的js方法如（打印方法），需要加载FineReport的js文件，实际情况下，一个页面中可能不仅有报表部分，还会加载您自己的js文件，为避免引起不必要的js冲突，我们建议将报表内容显示在Frame中，而不要显示在div中。这样调用FineReport内部的js方法时，可以不用引入FineReport的js文件，直接通过Frame获取报表再调用方法，具体可参考分页文档中自定义工具栏节点。