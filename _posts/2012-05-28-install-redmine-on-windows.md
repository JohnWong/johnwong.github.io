---
layout: post
title: Redmine on windows安装
category: Mobile
---

Redmine是用Ruby开发的基于web的项目管理软件，是用ROR框架开发的一套跨平台项目管理系统，据说是源于Basecamp的ror版而来，支持多种数据库，有不少自己独特的功能，例如提供wiki、新闻台等，还可以集成其他版本管理系统和BUG跟踪系统，例如SVN、CVS、TD等等。这种 Web 形式的项目管理系统通过“项目（Project）”的形式把成员、任务（问题）、文档、讨论以及各种形式的资源组织在一起，大家参与更新任务、文档等内容来推动项目的进度，同时系统利用时间线索和各种动态的报表形式来自动给成员汇报项目进度。
一直对Redmine心怀崇敬，所以就闲来无事试一试。参考[Redmine Install](http://www.redmine.org/projects/redmine/wiki/RedmineInstall)。环境如下：

为了不在配环境上浪费时间，我找到了[RailsInstaller](http://railsinstaller.org/)，Ruby和Rails都集成其中。使用railsinstaller-2.1.0。

```
Ruby 1.9.3-p125
Rails 3.2
Bundler 1.0.18
Git 1.7.6
Sqlite 3.7.3
TinyTDS 0.4.5
SQL Server support 3.3.3
MySQL 5.5
```

1. 安装RailsInstaller
2. 安装bundler，似乎安装了1就不必装这个了，以防万一又装了一下

```PowerShell
gem install bundler  
[ruby] view plaincopy
bundle install --without development test
```

3.安装rmagick

需要安装[imagemagick](http://www.imagemagick.org/script/binary-releases.php#windows)，参考[如何在Windows上安装rmagick](http://www.redmine.org/projects/redmine/wiki/HowTo_install_rmagick_gem_on_Windows)选择安装环境变量和C/C++头文件。

```PowerShell
set CPATH=C:\Program Files\ImageMagick-6.7.7-Q16\include  
set LIBRARY_PATH=C:\Program Files\ImageMagick-6.7.7-Q16\lib  
[ruby] view plaincopy
gem install rmagick or bundle install --without=development test, etc. 
``` 

4.创建mysql数据库

```sql
create database redmine character set utf8;  
create user 'redmine'@'localhost' identified by 'my_password';  
grant all privileges on redmine.* to 'redmine'@'localhost';
```

5. 复制config/database.yml.example到config/database.yml 修改 "production" 配置：

```ruby
production:  
  adapter: mysql2  
  database: redmine  
  host: localhost  
  username: redmine  
  password: my_password
```

6.创建session密钥

```PowerShell
rake generate_secret_token
```

7.创建数据库结构

```PowerShell
RAILS_ENV=production rake db:migrate
```

到这里卡主了。。。
找到问题是在windows下需要写成

```PowerShell
rake db:migrate RAILS_ENV="production"
```  

提示错误 couldn't parse YAML at line 18 column 2，这是因为修改database.yml的时候需要在每个冒号后需要加空格。
重新运行创建数据库，提示Incorrect MySQL client library version! This gem was compiled for 6.0.0 but the
client library is 5.5.20.
参考[StackOverflow](http://stackoverflow.com/questions/8740868/mysql2-gem-compiled-for-wrong-mysql-client-library)可以解决

然后继续报错Can't connect to MySQL server on 'localhost' (10061)

是因为使用ipv6导致localhost没指向到127.0.0.1，解决办法参考[StackOverflow](http://stackoverflow.com/questions/10792862/rails-development-cant-connect-to-mysql-server-on-localhost-10061)。

8.数据库载入默认数据

```PowerShell
rake redmine:load_default_data RAILS_ENV="production" 
```

选择语言的时候选zh

9.运行webrick web server测试安装

```PowerShell
ruby script/rails server webrick -e production 
```

至此安装完成 使用就以后再说。请看[演示地址](http://demo.redmine.org/)。初步使用，具有权限控制、多项目管理、提交bug、新建及分配任务、任务日历以及甘特图。