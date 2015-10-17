---
layout: category-basic
title: "书签"
---

<div class="post-poster">
    <img class="feature-img" alt="Bookmark" src="{{ "/images/bookmark.jpg" | prepend: site.cdnhost }}">
</div>

# 订阅资源
---

- [NSHipster](http://nshipster.cn)
- [Ray Wenderlich](http://www.raywenderlich.com/)
- [Objc.io](http://www.objc.io)
- [iOS Dev Weekly](https://iosdevweekly.com/)
- [iOS Development Tips](http://iosdevtips.co/)
- [Glow技术团队博客](http://tech.glowing.com/)
- [I'm TualatriX](http://imtx.me)
- [Kevin Blog](http://imkevin.me)
- [OneV's Den](http://onevcat.com)
- [Bang's Blog](http://feeds.feedburner.com)
- [Answer Huang](http://answerhuang.duapp.com)
- [唐巧的技术博客](http://blog.devtang.com)
- [不掏蜂窝的熊](http://www.hotobear.com)
- [念茜的博客](http://nianxi.net)

# 移动开发
---

#### [《Effective Objective-C 2.0：编写高质量iOS与OS X代码的52个有效方法》](http://book.douban.com/subject/21370593/)

> 关于OC开发非常不错的一本书。看过之后帮你有效减少bug。

#### [iOS头文件](http://developer.limneos.net/)

> 方便查询一些系统的类的信息，使用的是classdump。

#### [iOS字体](http://iosfonts.com/)

> 列出了iOS设备中字体及加入的版本。

#### [Apple开源](http://opensource.apple.com/)

> 一些苹果开源的类，比如可以查到NSString的hash实现。

#### [Zen and the Art of the Objective-C Craftsmanship](https://github.com/objc-zen/objc-zen-book)

> Objc的各种推荐用法。

#### [Leveling Up](https://www.bignerdranch.com/blog/leveling-up/)

> 对iOS开发进阶的忠告。

#### [github优秀开源项目大全-iOS](http://foggry.com/blog/2014/04/25/githubyou-xiu-xiang-mu-ios/)

> GitHub上用于iOS开发的各种项目。

#### [iOS开发中可以节省50%编译等待时间的几个措施](http://ios.jobbole.com/82124/)

> 通过使用`DWARF`而非`DWARF with dSYMFile`，不使用`–O4`优化标识来减少编译时间。

#### [watchOS API Blog](https://www.watchosapi.com/category/watchos/)

> 汇集了各种watchOS的API与知识。

#### [通知中心唤起设置等](http://www.iapps.im/jc/745.html)

> 原来iOS5可以使用的打开设置的链接依然存在，只是被屏蔽了。从通知中心就可以唤起了。

#### [提高iOS访问权限通过率](http://36kr.com/p/211441.html)

> 提高iOS访问权限通过率的方法介绍。

#### [Inside Code Signing](http://www.objc.io/issues/17-security/inside-code-signing/)

> 一篇比较老的介绍苹果代码签名机制的文章，包含了code sign、entitlement、provision profile等概念的介绍。

#### [绕过iPhone代码签名](http://www.saurik.com/id/8)

> Cydia创始人Jay Freeman写的绕过iPhone代码签名的文章。还有大神憋了好久做出来的工具[ldid](http://gitweb.saurik.com/ldid.git)。

#### [The technology behind preview photos](https://code.facebook.com/posts/991252547593574/the-technology-behind-preview-photos/)

> Facebook对弱网络下用户封面照片加载做了优化。将传统的获取URL、下载图片两次请求优化为第一次请求附带200字节图片。要实现图片限制在200字节内，使用了高速模糊、寻找合适的图片尺寸、选择了JPEG压缩格式、使用固定JPEG头不必每张图传输一次。中文译文[Facebook移动端照片预览背后的技术](http://www.infoq.com/cn/news/2015/08/facebook-photo-preview)省略了图片，并且部分内容有差别。

#### [String Localization](http://www.objc.io/issues/9-strings/string-localization/)

> objc.io上一篇字符串本地化文章。项目还是做本地化，需要掌握这方面的知识了。另外FauxPas挺不错，扫一下就能看到所有未做本地化的地方。

#### [如何检查iOS系统版本](http://stackoverflow.com/questions/3339722/how-to-check-ios-version/)

> 不要再这么写了：[[[UIDevice currentDevice] systemVersion] floatValue]

#### [让你快速上手Runtime
](http://www.jianshu.com/p/e071206103a4)

> Runtime的文章先收藏，还没来得及看。

#### [Sublime Text插件](http://www.zhihu.com/question/24736400)

# 效率提升
---

#### [打造高效的 Finder](http://zhuanlan.zhihu.com/MacTips/20130167)

> Finder使用中确实有不便之处。微小的改变带来不错的效果。

#### [你应该知道的 iTerm2 使用方法](http://wulfric.me/2015/08/iterm2/)

> 用了iTerm2后就再也不碰原生Terminal了。高级用法还在学习中。

#### [](https://codeanywhere.com/)

> 现在看起来最棒的在线写代码平台，支持多种语言，多种操作系统。

#### [在线编译器](http://www.compileonline.com/)

> 如果你想尝试一门语言，又不想在自己电脑上安装一堆运行时环境，那么试试在线编译器吧，浏览器就够了。

#### [Codding Ground](http://www.tutorialspoint.com/codingground.htm)

> 另一个在线写代码的平台。

#### [解决Xcode下载Simulator, Doc慢的问题](http://www.cnblogs.com/Roki/p/4620623.html)

> 用Charles解决下载慢的问题。目前用的代理还可以，下载速度暂时不用担心。

#### [Sublime Text](http://www.sublimetext.com/)

> 非常好用的编辑器。Sublime Text 2可以免费试用。一定要安装[Package Control](https://packagecontrol.io/installation)。

# 逆向与安全
---

#### [《iOS应用逆向工程：分析与实战》](http://book.douban.com/subject/25826902/)

> 首推这本书，很快可以看完。收获不少。

#### [逆向工程工具](http://iphonedevwiki.net/index.php/Reverse_Engineering_Tools)

> 逆向工程工具科普。

#### [反编译工具下载](http://down.52pojie.cn/Tools/Disassemblers/)

> 下载一系列反编译工具。

#### [钟馗之眼](http://www.zoomeye.org/)

> 让你像Google搜索一样寻找漏洞。

#### [xmd5.org](http://www.xmd5.org/)

> 目前看起来最好的md5反查网站。

# 视觉交互资源
---

### 图标
---

#### [Iconfont](http://iconfont.cn/)

> 寻找图标的第一选择，异常丰富。

#### [FlatIcon](http://www.flaticon.com/)

> 图标丰富，支持多种格式，比如Iconfont、PNG、SVG、EPS、PSD。

#### [IconsDB](http://www.iconsdb.com/)

> 图标丰富，有不少成套图标。

#### [App Icon Template](http://www.appicontemplate.com/)

> 应用图标的PSD模版，非常推荐。

#### [Fort Awesome Kit](http://fortawesome.github.io/Font-Awesome/icons/)

> 另一个icon font的网站，图标不少但是导出png略烦。

#### [1624 Gorgeous Swifticons Icons](http://www.mightydeals.com/deal/swifticons.html)

> 语哥推荐的收费图标，最终还是花了29刀买下了。

### [IconStore](http://iconstore.co/)

> 微博上发现的图标网站，逼格很高。

### 视觉设计
---

#### [Do UI Kit](http://www.invisionapp.com/do)

#### [Uber商标指南](http://brand.uber.com/)

#### [Dropbox商标指南](https://www.dropbox.com/branding)

#### [免费badge设计](http://www.cssauthor.com/free-badges/)

#### [谷歌设计的Sketch教程](https://medium.com/google-design/sketch-tutorial_01-b76271a095e3)

#### [应用设计库](http://www.appdesignvault.com/)

#### [千图网](http://www.58pic.com/)

> 一个国内的免费素材网站。

#### [求字体](http://www.qiuziti.com/)

> 根据图片识别出所使用的字体。

#### [cfxr](http://thirdcog.eu/apps/cfxr)

### 交互设计
---

#### [Origami官方文档翻译](http://www.ui.cn/detail/43336.html)

#### [原型设计工具Framer](http://framerjs.com/)

### 其他资源
---

> 构建声音特效。

#### [Texture Packer](https://www.codeandweb.com/texturepacker/download)

> 构建Sprite图，可以用在前端与Cocos2d-x上。

#### [Subtle Patterns](http://subtlepatterns.com/)

> 纹理贴图。

#### [Audio Tutorial for iOS: Converting and Recording](http://www.raywenderlich.com/69367/audio-tutorial-ios-converting-recording-2014-edition)

> 声音效果知识与工具。

#### [Cloud Convert](https://cloudconvert.com/mov-to-gif)

> 不错的文件转换工具，mov转gif用于markdown，压缩率不错。

# 其他
---

#### [archive.org](http://archive.org/web/)

> 查找网站的历史快照。很强大。

#### [在线解密](http://riddle.arthurluk.net/express/love.php)

> IT屌丝无聊了玩这个最开心了

#### [Geoguessr](https://geoguessr.com/)

> 谷歌街景，把你扔到荒郊野外，去推测自己所在的位置。





