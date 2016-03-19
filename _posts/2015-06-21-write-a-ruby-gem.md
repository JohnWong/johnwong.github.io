---
layout: post
title: 学习编写Ruby gem
category: mobile
description: 假期get新技能，编写Ruby gem
thumb: /images/2015-06-21-write-a-ruby-gem.png
---

之前写过一个IP反查地理位置的服务[http://pytool.sinaapp.com/](http://pytool.sinaapp.com/)。在命令行中使用的时候经常需要先根据域名反查ip。然后浏览器打开反查地理位置的网址，拼接ip。于是想把这个功能封装到命令行里。比较好的平台有Ruby gem与npm。最后选择了Ruby gem。

## 安装RVM

RVM是一个Ruby环境管理器。可以参考[安装方法](https://github.com/rvm/rvm#installation)，如下：

```
curl -L https://get.rvm.io | bash -s stable --autolibs=enabled
```

## 新建RVM gemset

这个功能的名字使用ip2location比较贴切，但是用`gem search`查过已经存在。最终使用名字`ip2l`。

```
rvm gemset create ip2l  
rvm gemset use ip2l 
```

## 打包gem

bundler是一个管理gem依赖，创建gem模版的好工具。安装也非常简单：

```
gem install bundler
```

然后创建我们的gem：

```
bundle gem ip2l
```

目录内文件结构为：

```
├── Gemfile
├── Gemfile.lock
├── README.md
├── Rakefile
├── bin
│   ├── console
│   └── setup
├── ip2l.gemspec
└── lib
    ├── ip2l
    │   └── version.rb
    └── ip2l.rb
```

甚至连README都生成好了，非常规范，内容齐全。需要做的仅仅是替换掉一些TODO。

## 编写module

在ip2l.rb内添加类来实现服务调用：

``` ruby
require "ip2l/version"
require 'net/http'
require 'json'

module Ip2l
  class Ip2l
    def ip_to_location(ip)
      uri = URI("http://pytool.sinaapp.com/geo?type=json&pos=1&encoding=utf-8&ip=%s" % ip)
      content = Net::HTTP.get(uri)
      result = JSON.parse(content)
      result["geo"]["loc"]
    end
  end
end
```

## 编写可执行文件

在bin下添加文件ip2l。用optparse可以实现对命令行参数的解析。不过实际使用中发现optparse有很多不好用的地方。参数必填按照[Stackoverflow上一个方案](http://stackoverflow.com/questions/1541294/how-do-you-specify-a-required-switch-not-argument-with-ruby-optionparser/1542658#2149183)解决。希望可执行文件名后直接跟一个参数，看起来不支持，手动解析了。在参数校验成功后调用之前编写的module反查并输出。

```
ip2l = Ip2l::Ip2l.new
puts ip2l.ip_to_location(ip)
```

## Gemspec

Gemspec的作用类似CocoaPods的Podspec。模版生成的文件已经放了不少TODO，根据需要自行替换成真实的信息。另外需要修改两行来指明可执行文件所在位置：

```
  spec.bindir        = "bin"
  spec.executables   = ["ip2l"]
```

## 校验与上传

执行`rake install`，之后命令行中应该已经可以使用了。如果希望发布到RubyGems.org，那么需要处理Gemspec中的发布限制。最简单的方法就是按照注释移除`allowed_push_host`部分。确保没问题后就可以使用`rake release`发布了。可能会遇到需要登录的问题。只需要到RubyGems.org注册一下，发布的时候登录一次就好了。

发布后马上就可以搜到了，地址是[https://rubygems.org/gems/ip2l](https://rubygems.org/gems/ip2l)。写博的时间内已经有22的下载了。

## 写在最后

Ruby gem的工具集非常完善，做下来非常轻松。感觉CocoaPods的发布应该是参考了Ruby gem。以前总觉得Python语法舒服，库齐全，无法比拟。现在看起来Ruby也不差。

安装RVM后发现Ruby和gem都变成了RVM安装的版本，以前安装的一些gemset出问题了。简单改Ruby的链接后一堆问题，干脆Ruby和gemset都使用RVM的版本，重装了一些gem后看起来没问题了。