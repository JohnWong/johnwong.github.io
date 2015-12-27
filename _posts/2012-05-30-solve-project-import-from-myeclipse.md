---
layout: post
title:  从MyEclipse导入Eclipse导致不能识别为web项目
category: Past
description: 老师给的实例代码由MyEclipse生成。导入MyEclipse之后识别为Java项目。
---

老师给的实例代码由MyEclipse生成。导入MyEclipse之后识别为Java项目。可以新建项目，然后把对应的配置文件、java源文件和页面文件放入相应目录，但是不想这么做。解决方法从网上找到了。

1. 进入项目目录，找到.project文件，打开。 找到 `<natures>...</natures>` 代码段。 加入如下标签内容并保存： 

```xml
<nature>org.eclipse.wst.common.project.facet.core.nature</nature> 
<nature>org.eclipse.wst.common.modulecore.ModuleCoreNature</nature> 
<nature>org.eclipse.jem.workbench.JavaEMFNature</nature> 
```

2. 在eclipse的项目上点右键，刷新项目。在项目上点右键，进入属性（properties） ，在左侧列表项目中点击选择“Project Facets”，在右侧选择“Dynamic Web Module”和"Java"，点击保存即可。

3. 如果项目的webroot跟默认的不符合，修改一下配置。

打开项目的.settings\org.eclipse.wst.common.component文件，把里面默认的webContent改成自己自定义的目录名。 

进入项目目录，找到.project文件，找到output目录的设定，修改成自定义的目录名，例如

```xml
<classpathentry kind="output" path="web/WEB-INF/classes"/>
```