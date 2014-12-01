---
layout: post
title:  MySQL重置root密码
category: Mobile
---

1. 停止mysql服务(以管理员身份,在cmd命令行下运行)使用如下命令：

```PowerShell
net stop mysql
```
![stop mysql service](http://yspe2371e4aa7697989.yunshipei.cn/dHlwZT1mdyZzaXplPTY0MCZzcmM9YUhSMGNDVXpRU1V5UmlVeVJuZDNkeTVxWWpVeExtNWxkQ1V5Um5Wd2JHOWhaQ1V5UmpJd01USXdNU1V5UmpJd01USXdNVEUwTWpFeE5qSTVNalUyTG1wd1p3PT0=)

2. 使用命令启动mysql数据库，命令如下

```PowerShell
mysqld - -skip-grant-tables
```

![restart mysql](http://yspe2371e4aa7697989.yunshipei.cn/dHlwZT1mdyZzaXplPTY0MCZzcmM9YUhSMGNDVXpRU1V5UmlVeVJuZDNkeTVxWWpVeExtNWxkQ1V5Um5Wd2JHOWhaQ1V5UmpJd01USXdNU1V5UmpJd01USXdNVEUwTWpFeE5qSTVOakF4TG1wd1p3PT0=)

3. 新开一个cmd窗口，进行如下命令操作

```PowerShell
mysql -uroot
update mysql.user set password=password('root') where user='你的密码';
```

![reset password](http://yspe2371e4aa7697989.yunshipei.cn/dHlwZT1mdyZzaXplPTY0MCZzcmM9YUhSMGNDVXpRU1V5UmlVeVJuZDNkeTVxWWpVeExtNWxkQ1V5Um5Wd2JHOWhaQ1V5UmpJd01USXdNU1V5UmpJd01USXdNVEUwTWpFeE5qSTVNVGMyTG1wd1p3PT0=)

4. 打开任务管理器，停止mysql,mysqld进程，使用net start mysql启动mysqld服务，就可以使用root用户 root密码进入数据库了（这步可以省略重启机器）