---
layout: post
title: Java代码签名与认证
category: Mobile
---

看了这一章的内容，觉得有的部分很熟悉，因为Android的签名认证就是使用的java的这一机制。签名和认证的过程如图：

至于公钥和私钥加密解密的过程和原理有待进一步研究。签名和认证的示例如下：

1. 编写类Friend和Stranger继承字Doer
2. 将Friend和Stranger分别打成jar包

```PowerShell
jar cvf friend.jar com/artima/security/friend/*.class  
jar cvf stranger.jar com/artima/security/stranger/*.class
```

3. 生成两个密钥对

```PowerShell
keytool -genkey -alias friend -keypass friend4life -validity 10000 -keystore ijvmkeys  
keytool -genkey -alias stranger -keypass stranger4life -validity 10000 -keystore ijvmkeys
```

两次输入的密码需要一致。因为第二次添加key的时候需要访问keystore，于是就需要第一次设定的密码。
4. 使用jarsigner签名

```PowerShell
jarsigner -keystore ijvmkeys -storepass ijvm2ed -keypass friend4life friend.jar friend  
jarsigner -keystore ijvmkeys -storepass ijvm2ed -keypass stranger4life stranger.jar stranger
```
 
签名过的jar包，修改其中的内容后，运行该jar包会报java.lang.SecurityException异常。