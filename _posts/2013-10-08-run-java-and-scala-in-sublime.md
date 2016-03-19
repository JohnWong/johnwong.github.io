---
layout: post
title: "Sublime中编译运行java和scala"
category: past
description: 了解Sublime神器。
---
1\. 运行Java参考[http://www.oschina.net/translate/compile-and-run-java-programs-in-sublime-text-2](http://www.oschina.net/translate/compile-and-run-java-programs-in-sublime-text-2)

a. 设置环境变量

b. 在jdk的bin目录或者其他path中新建编译运行脚本

windows下runJava.bat:

```bash
@ECHO OFF
cd %~dp1
ECHO Compiling %~nx1.......
IF EXIST %~n1.class (
DEL %~n1.class
)
javac %~nx1
IF EXIST %~n1.class (
ECHO -----------OUTPUT-----------
java %~n1
)
```


linux下runJava.sh:

```bash
[ -f "$1.class" ] && rm $1.class
for file in $1.java
do
echo "Compiling $file........"
javac $file
done
if [ -f "$1.class" ]
then
echo "-----------OUTPUT-----------"
java $1
else
echo " "
fi
```

c. Preferences > Browse Packages.. 打开sublime的包目录，将JavaC.sublime-build中javac命令替换为runJava.bat或者runJava.sh

2\. 运行scala

a. Tools->Build System->new Build System，保存到Packages的scala目录中，写入内容：

```
{
	"cmd": ["scala", "$file"],
	"windows":{
		"cmd": ["scala.bat", "$file"]
	}
}
```

b. 打开scala文件按ctrl&#43;B就可以看到运行结果。

