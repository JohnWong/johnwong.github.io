---
layout: post
title: 用FauxPas找到潜在Bug
category: Mobile
description: 一个不错的Xcode检查工具，只是略贵。
thumb: "/images/2014-08-29-using-fauxpas.jpg"
---
Faux Pas是一个Xcode辅助工具，检查iOS或者Mac项目，找到潜在bug，以及可维护性和风格问题。提供了92条规则可供挑选，支持GUI和CLI。目前发布了beta版，提供30天试用。

[Faux Pas Homepage](http://fauxpasapp.com/)
[Faux Pas Donwload](http://fauxpasapp.com/try/)

亲身试用后，发现了项目中的多处问题。一些需要手动查找的问题，在这里都得到了检查。同时也提供了代码风格的建议和一些细节的优化建议。

## 功能

 - 控制潜在bug
 - 查找资源文件错误
 - 查找本地化错误
 - 发现版本控制错误
 - 学习和实施最佳实践
 - 实施代码风格
 - 代码审查清单
 - 92条规则可供挑选
 - 提供GUI或者CLI
 - 在Xcode构建时运行
 - 连接外部工具，支持导出结果和自定义脚本
 - 按标签选取规则 保存在JSON配置文件中
 - 更改打开代码的编辑器

## 使用方法

### GUI

 - 打开FauxPas
 - 选择或者排除一些规则
 - Start Checking
    
### CLI

 - 打开FauxPas
 - 菜单栏Faux Pas > Install CLI Tools…
 - shell> fauxpas -t iCoupon check iCoupon.xcodeproj/
 - 可以输出不同格式、挑选检查规则等，参见帮助，例如查找重复资源

 ```
 fauxpas --onlyRules UnusedResource -o json check MyProject.xcodeproj
 ```
 
### Xcode build时检查

 - 确保CLI安装
 - 在Xcode项目的target中新增"Run Script" build phase
 - 添加如下脚本，build时会执行FauxPas检查
  
```
[[ ${FAUXPAS_SKIP} == 1 ]] && exit 0

 FAUXPAS_PATH="/usr/local/bin/fauxpas"
 if [[ -f "${FAUXPAS_PATH}" ]]; then
   "${FAUXPAS_PATH}" check-xcode
 else
   echo "warning: Faux Pas was not found at '${FAUXPAS_PATH}'"
 fi
```
建议不使用这种方式，会额外增加build时间。

### Xcode中手动执行

 - 确保CLI安装
 - 项目中创建Aggregate类型target
 - 在该target下新增"Run Script" build phase
 - 添加如下脚本，运行该target时会执行FauxPas检查
 
 ```
 /usr/local/bin/fauxpas -o xcode check "PROJECT_NAME.xcodeproj"
 ```
 
### 导出结果

 - GUI中点击Export Diagnostics，选择格式
 - CLI下-o参数，可选human、json、plist、xcode
 - 导出结果可以用其他工具处理

## 实战

使用GUI扫描了项目，发现了许多不少有价值的问题，值得我们学习。

 - 编译参数的有益建议，比如-DNDEBUG
 - 多处图片缺少和图片重复
 - 非retian与retina图尺寸不是2倍
 - 没有前缀或者前缀与SDK冲突，建议至少三字符长度
 - Retain Delegate
 - 重载或者调用一些限制的系统方法
 - 缺少获取授权的描述
 - Category方法冲突
 - 未使用的Error值，建议不关心Error时参数传入NULL
 - 设置delegate或者datasource为self时需要在dealloc中置为空
 - 对指针和0做比较
 - obj ? obj : other obj将会评估2次。而obj ?: other会评估一次
 - 界面字符串缺少本地化，我们的项目实际不需要
 - 修改传入参数的值
 - model类包含的对象的@property建议用copy，防止非setter的修改
 - pch中引用过的头文件再次引用多余
 - VCS建议，例如建议Xcode workspace data不忽略
 - 在init or dealloc不要使用setter。
 - 不和习惯的getter。使用something而非getSomething
 - 旧语法，例如+[NSNumber numberWithFloat:], -[NSDictionary objectForKey:]。建议转换为现代语法Edit → Refactor → Convert To Modern Objective-C Syntax