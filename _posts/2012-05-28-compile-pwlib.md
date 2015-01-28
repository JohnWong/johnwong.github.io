---
layout: post
title: "Pwlib编译"
category: Past
description: Pwlib编译
---
参考文档有http://www.voxgratia.org/docs/pwlib_windows.html#download 和 http://www.cnblogs.com/VOIP/archive/2010/04/30/1724665.html 

1.使用VS2005，最新版pwlib http://sourceforge.net/project/showfiles.php?group_id=80674和winzip。 

2.ptlib-v1_12_0-src.zip解压到D盘。到http://www.voxgratia.org/bin/flexbison.zip下载后解压到C盘根目录。 

3.因为同时安装了VC6和VS2005了，所以需要添加环境变量VSNET2005_PWLIB_CONFIGURE_EXCLUDE_DIRS C:\Program Files\Microsoft Visual Studio来排除VC6的目录。用VS2005打开ptlib根目录下的pwlib_2005.sln。 
将目录“C:\TOOLS”添加到IDE的“Executable Directories”中 
将installdir\PWLIB\INCLUDE 添加到VC的 Include 目录列表 
将installdir\PWLIB\LIB 添加到VC的 Executable目录列表 
将installdir\PWLIB\LIB 添加到VC的 Library目录列表 

4.Ptlib可选包有一堆，我安装了OpenSSL(http://www.slproweb.com/products/Win32OpenSSL.html ),Expat(http://sourceforge.net/project/showfiles.php?group_id=10127 ),OpenLDAP(http://www.voxgratia.org/bin/openldap-2.1.17_bin.zip),IPV6和DNSResolver已经在VS2005中得到了支持。编译后能不能使用这些特性还没有试过。 

5.先单独编译Configure分别用Debug和Release 的版本.记得是仅编译(Configure项目). 

6.编译 PTLib Static 

7.编译MergeSym项目。把生成的MergeSym.exe可执行文件 复制到\ptlib\src\ptlib\msos文件下面

8.编译PTLib Dll 

9.在Lib目录下面生成了编译好的库文件 
(PTLib Static的Debug和Release版本) ptlibsd.lib，ptlibs.lib 
(PTLib DLL的Debug和Release版本) (PTLibd.lib.PTLibd.dll) (PTLib.lib.PTLib.dll )

国庆放假回家了，剩下的OpenH323等回来再做。

