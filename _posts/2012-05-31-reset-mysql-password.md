---
layout: post
title:  MySQL重置root密码
category: Past
description: 重置MySQL的root密码
---

1. 停止mysql服务(以管理员身份,在cmd命令行下运行)使用如下命令：

```PowerShell
net stop mysql
```

2. 使用命令启动mysql数据库，命令如下

```PowerShell
mysqld - -skip-grant-tables
```

3. 新开一个cmd窗口，进行如下命令操作

```PowerShell
mysql -uroot
update mysql.user set password=password('root') where user='你的密码';
```

4. 打开任务管理器，停止mysql,mysqld进程，使用net start mysql启动mysqld服务，就可以使用root用户 root密码进入数据库了（这步可以省略重启机器）