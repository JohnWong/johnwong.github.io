---
layout: post
title:  Android Studio踩坑记
category: Mobile
---

拾起Android项目，需要使用Goolgle Play Services。顺应潮流换了Android Studio，开启了踩坑之旅。

1. 尝试直接将Eclipse项目导入AS，结果根本没法用啊。正确的方法应该是升级ADT，在Eclipse下导出build.gradle然后再导入。但是升级的时间还不如直接新建项目把资源拷进去，同时也能了解一下AS默认的项目结构。

2. 第一个遇到的问题是新建的项目没有assert和lib目录。java和res等资源都在src/main目录下，于是我将assets和libs目录都放在这了。结果assets目录没问题，但是实际上要在gradle文件中引用libs目录，libs目录应该放在src下。

3. 加入jar包没有那么简单，放入libs目录下之后还需要：右击lib选择添加为lib；在项目中添加库引用；在build.gradle中添加对这个jar的依赖；手动在项目目录下运行gradew clean。

4. 想要使用gms，最新的方法是在SDK manager中安装Google Play Services和Google Repository，在dependencies中添加：

    compile 'com.android.support:support-v4:19.0.0'
    compile 'com.android.support:appcompat-v7:19.0.0'
    compile 'com.google.android.gms:play-services:4.1.32'

5. 这里的版本号也是略坑爹，想知道版本号需要打开目录<SDK>\extras\google\m2repository\com\google\android\gms\play-services，然后就能看到可用的版本号，其他两个包也是类似的方法查看。

6. 下载的play services目录重要示例工程，本还想参考一下，结果都没有升级成新的工程结构。

7. Play Services安装文档中指明需要添加：

<meta-data android:name="com.google.android.gms.version"
           android:value="@integer/google_play_services_version" />
但是这个版本号略坑。平时看到的都是x.x.xx这样的格式，而不是整数。最终在sdk\extras\google\google_play_services\libproject\google-play-services_lib\AndroidManifest.xml中找到了版本号4132530，运行之后提示需要的是4132500，为什么要减去30至今没搞明白。需要放在application节点下，我还错误地放在manifest节点下。

最后吐槽一下打开的各种弹窗太大了，我这1366×768分辨率的笔记本经常看不到下边的内容。第一次运行AS的时候还有长时间走滚动条的问题，据说是在下载gradle，不过我没有感觉到。因为用电脑是需要和小外甥打游击，不能被看到，下载的时候把电脑藏起来干别的去了。

jni库始终无法正常加入安装包中。没事升级AS到0.4.3，之前jar包引用又出问题了，就在决定今天无法解决就换回Eclipse之际，一篇帖子帮了大忙：http://blog.csdn.net/look_down/article/details/17557031

1. build.gradle中gradle版本修改为0.7+

2. 运行后出错，按照提示修改gradle-wrapper.properties文件中

3. 加入so库的代码修改为：

task copyNativeLibs(type: Copy) {  
    from fileTree(dir: 'libs', include: 'armeabi/*.so' )  into  'build/lib'  
}  
tasks.withType(Compile) {  
    compileTask -> compileTask.dependsOn copyNativeLibs  
}  
  
clean.dependsOn 'cleanCopyNativeLibs'  
  
tasks.withType(com.android.build.gradle.tasks.PackageApplication) { pkgTask ->  
   pkgTask.jniFolders = [new File(buildDir, 'lib')]  
}  
经过gradlew clean build之后成功了。这下没有理由再用Eclipse了。