---
layout: post
title: "signavio-core-components ant build-all-in-one-war failed"
category: Past
description: 最近搞了下signavio-core-components项目，遇到了一些问题。
---
最近搞了下signavio-core-components项目，网址是http://code.google.com/p/signavio-core-components

执行`ant build-all-in-one-war`或者`ant build-and-deploy-all-in-one-war-to-tomcat`

```
BUILD FAILEDD:\signavio\build.xml:64: The following error occurred while executing this lineD:\signavio\editor\build.xml:118: Java returned: 2
```

研究了一下是因为编码问题，ant文件调用了editor/build.xml。其中有

```
<concat destfile='${build}/oryx.debug.js'>...</concat>
```

这个命令是合并文件，但是源文件中的scripts/Core/SVG/label.js是utf-8&#26684;式的，而其他是ansi&#26684;式的，这个utf-8文件转成ansi会出现乱码。因此修改为

```
<property name="charset" value="utf-8"/>
<concat destfile='${build}/oryx.debug.js' encoding="${charset}" outputencoding="${charset}">

<java dir="${build}" jar="${root}/lib/yuicompressor-2.4.7.jar" fork="true" failonerror="true" output='${compress.temp}'>
```

解决办法同样PO在了项目issue中，参见

http://code.google.com/p/signavio-core-components/issues/detail?can=2&;start=0&;num=100&;q=&;colspec=ID%20Type%20Status%20Priority%20Milestone%20Owner%20Summary&;groupby=&;sort=&;id=29

http://code.google.com/p/signavio-core-components/issues/detail?can=2&;start=0&;num=100&;q=&;colspec=ID%20Type%20Status%20Priority%20Milestone%20Owner%20Summary&;groupby=&;sort=&;id=29

