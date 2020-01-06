---
layout: post
title: "使用IconFont减小iOS应用体积"
category: mobile
description: 既然IconFont项目已经开源，那么文章也可以发出来啦
thumb: /images/2015-04-03-using-icon-font-in-ios.png
---

点点iOS项目本身功能较多，导致应用体积也比较大。但是手机淘宝集成时对插件包大小有要求。因此点点iOS团队使用了一些方法来缩小插件包体积，比如部分业务只放在独立版、图片压缩（PNG大图转成JPG，ImageAlpha与ImageOptim对PNG图片压缩）、部分大图安装后从网络下载。近期小虎提出使用IconFont技术减小图片体积，让我在这这方面做了一些研究。最终将IconFont应用在iOS项目中，取得了不错的效果。如果你懒得看这么长的文，那么直接去看[IconFont项目]吧。

## 简介

IconFont技术起源于Web领域的Web Font技术。随着时间的推移，网页设计越来越漂亮。但是电脑预装的字体远远无法满足设计者的要求，于是Web Font技术诞生了。一个英文字库并不大，通过网络下载字体，完成网页的显示。有了Web Font技术，大大提升了设计师的发挥空间。

网页设计中图标需要适配多个分辨率，每个图标需要占用一次网络请求。于是有人想到了用Web Font的方法来解决这两个问题，就是IconFont技术。将矢量的图标做成字体，一次网络请求就够了，可以保真缩放。解决这个问题的另一个方式是图片拼合的Sprite图，他们之间的对比参考[Image Sprites vs Web IconFonts]。

在iOS项目中应用IconFont主要目的是缩小图片所占体积。尝试用[TexturePacker]将点点的七百多图片拼合为Sprite图，体积只减少了几十KB，还未计算需要增加的代码量，实际帮助很小。而IconFont在这方便帮助很大。我们在项目中应用IconFont后取得了不错的效果，后面会做详细的体积减小效果统计。目前新功能开发中的图片都尽量采用IconFont来实现。IconFont应用在iOS中的优点和缺点如下：

### 优点
- 减小体积，字体文件比图片要小
- 图标保真缩放，解决2x/3x乃至将来的nx图问题
- 方便更改颜色大小，图片复用

### 缺点
- 只适用于`纯色icon`
- 使用unicode字符难以理解
- 需要维护字体库

## 字体管理

字体管理方式分为两种：在线管理（[iconfont.cn]）和FontForge工具。在实际应用中我们采用了在线管理的方式。

### 在线管理

[iconfont.cn]网站可以方便地在线管理字库，使用方法参考[iconfont.cn帮助]。在帮助中为设计师提供了`图标制作说明`和`模版文件下载`。帮助中给出了iOS应用的方法，只是简单地用UILabel显示图标，还远不够好用，在`应用于客户端`一节我们介绍如何更灵活地应用。

考虑到与设计师的协作、工程师之间的协作，最终我们采用了这种管理方式。协作过程中角色包括设计师、字体管理者（某个开发者兼任）、开发者。整个流程环节包括：上传、分发、加入工程、开发。

上传：在[iconfont.cn]网站上创建一个共用项目，设计师将图标上传这个项目中，并调整好图标的位置。建议在图标的上下左右边界留出一点空白，以确保图标显示完整。iconfont.cn上的字体一般在四个方向留下1/16的空白，如下图所示。修改图标位置大小的方法是在上传的图标上悬停，点击弹出的编辑按钮。编辑窗口可以调整图标的大小、位置、旋转角度。缩放和移动的粒度通过右上角网格尺寸来控制，例如填写16时一次调整粒度是图标的1/16。

![iconfont_cn_edit](/images/2015-04-03-using-icon-font-in-ios-iconfont-edit.png)

分发：
iOS与Android团队分别建立各自的项目，由各自的字体管理者将共用项目中各自用到的图标导入到建立的项目中。以后有新图标需要加入时，分发的工作也可以由用到新图标的开发者自行加入导入项目。

加入工程：每次更新图标后由字体管理者下载字体，加入到工程中并提交到工程的版本控制系统。如果希望更进一步压缩字体体积，可以用FontForge简化字体（用FontForge打开字体，Ctrl+A，Element -> Simplify -> Simplify）。

开发：开发人员使用字体中的图标完成开发。开发这一步可以与加入工程同时进行。因为分发结束后图标的Unicode码已经可以在网站上看到，开发可以先行开发，只是暂时看不到结果。

### FontForge工具

[FontForge]是一个自由免费的工具，支持Linux/Mac/Windows（Mac下基于X11，Windows下基于MSYS）。不仅易于上手适合初学者学习字型设计，而且也提供了一系列高级工具。下图为FontForge的主界面和绘制窗口。更详细的帮助参考[Design With FontForge]。使用FontForge制作字体的过程如下。

![fontforge_overview](/images/2015-04-03-using-icon-font-in-ios-fontforge-overview.png)

![fontforge_draw](/images/2015-04-03-using-icon-font-in-ios-fontforge.png)

#### 1. 调整配置

为了确保字体正确显示，需要调整字体文件的一些参数。

 - 字体名称：FontForge -> Element -> Font Info... -> PS Names，将PS Names、Family Name和Name For Humans三个属性改为你想使用的字体名称。

Note. 使用字体时一般可以根据字体名称取到字体。这个字体名称存储在字体文件内部，与字体的文件名无关。在Mac下查看字体名称最简单的方法就是双击字体用默认打开程序Font Book打开，窗口标题栏会显示字体名称。为了定制取字体时用到的字体名称，我们需要修改字体的名称。建议将PS Names下的PS Names、Family Name和Name For Humans三个属性都修改了，以避免与项目中其他字体冲突。只改第一个或者前两个可能出现异常，比如应用切到后台再切回来会出现其中一个字体显示异常的问题。

- 字体大小：FontForge -> Element -> Font Info... -> General。建议配置：

```
Ascent: 812
Descent: 212
EM Size: 1024
```

- 字体偏移量：FontForge -> Element -> Font Info... -> OS/2 -> Metrics，Is Offset勾选，并且相应的输入框填0。

#### 2. 矢量文件导出为SVG

[FontForge]支持导入的常用矢量图格式有EPS、SVG、PDF等。需要将AI文件转化为SVG文件后导入（AI文件转为EPS后导入，程序崩溃了。打开EPS文件直接粘贴，不能正常显示。）。一些导出SVG的优化选项参考[AI导出SVG的优化]。

#### 3. 将SVG导入字库

- 双击放置图标的字符，打开字型绘制窗口
- 导入SVG文件，File -> Import...，类型选择SVG
- 适当调整导入的曲线的位置，最终显示区域为窗口中央的正方形
- 完成后关闭字形绘制窗口

#### 4. 添加填充字形

目前发现如果没有字符达到Ascent与Descent两个位置，字型位置会下移。暂时解决方法是选择一个字符填充到这两个位置，即使超过也没关系。我们选择了通常会填充的字符X。缺少这个字符的字体使用在网页上，XP上的Safari浏览器会引起操作系统崩溃。

#### 5. 导出字体文件

File -> Generate Fonts。本文始终使用TrueType字体展开研究，所以类型选择TrueType。iOS也支持odf字体，有兴趣的读者可以尝试。

## 应用于客户端

### 字体注册

iOS中使用自定义字体，将字体加入项目后，还需要注册字体。注册的方式有两种：－ 在Info.plist中声明"Fonts provided by application"
－ 调用API来注册。考虑到需要支持独立版和插件版，调用API注册更加方便。字体注册和获取的代码如下：

```
+ (void)registerFontWithURL:(NSURL *)url {
    NSAssert([[NSFileManager defaultManager] fileExistsAtPath:[url path]], @"Font file doesn't exist");
    CGDataProviderRef fontDataProvider = CGDataProviderCreateWithURL((__bridge CFURLRef)url);
    CGFontRef newFont = CGFontCreateWithDataProvider(fontDataProvider);
    CGDataProviderRelease(fontDataProvider);
    CTFontManagerRegisterGraphicsFont(newFont, nil);
    CGFontRelease(newFont);
}

+ (UIFont *)fontWithSize:(CGFloat)size {
    UIFont *font = [UIFont fontWithName:[self fontName] size:size];
    if (font == nil) {
        [self registerFontWithURL: [[NSBundle mainBundle] URLForResource:[self fontName] withExtension:@"ttf"]];
        font = [UIFont fontWithName:[self fontName] size:size];
        NSAssert(font, @"UIFont object should not be nil, check if the font file is added to the application bundle and you're using the correct font name.");
    }
    return font;
}
```

### 字体应用方式

可能的应用方式：

- UILabel作为Icon
- UIButton的titleLabel作为Icon
- 根据字体生成UIImage

在实际项目中，我们采用了第三种方式。因为生成UIImage更加灵活，可以替代UIImage，而不是更外层的UIImageView。我们采用Category的方式为UIImage添加方法，根据图片大小、颜色和Unicode码来生成并返回图片。这个方法的代码如下，其中TBCityIconInfo是一个存储图片信息类：

```
+ (UIImage *)iconWithInfo:(TBCityIconInfo *)info {
    CGFloat size = info.size;
    CGFloat scale = [UIScreen mainScreen].scale;
    CGFloat realSize = size * scale;
    UIFont *font = [TBCityIconFontUtil fontWithSize:realSize];
    UIGraphicsBeginImageContext(CGSizeMake(realSize, realSize));
    CGContextRef context = UIGraphicsGetCurrentContext();
 
    if ([info.text respondsToSelector:@selector(drawAtPoint:withAttributes:)]) {
        [info.text drawAtPoint:CGPointZero withAttributes:@{NSFontAttributeName:font, NSForegroundColorAttributeName: info.color}];
    } else {
        CGContextSetFillColorWithColor(context, info.color.CGColor);
        [info.text drawAtPoint:CGPointMake(0, 0) withFont:font];
    }
    
    UIImage *image = [UIImage imageWithCGImage:UIGraphicsGetImageFromCurrentImageContext().CGImage scale:scale orientation:UIImageOrientationUp];
    UIGraphicsEndImageContext();
    
    return image;
}
```

### API设计

[FontasticIcons]对API的设计是，预先定义方法，方法名包含图片名称。在运行时为类添加这些方法的实现。图片名称到Unicode字符的映射，采用iOS本地化文件。映射文件编译的时候会压缩，不会占用过多体积。

我们通过一个类TBCityIconInfo来保存一张图片的大小、颜色和Unicode码。在一个文件中定义了一些宏，在这些宏中做这些信息的组合。这样字体定义放在一起方便查找管理，用到图片的地方只需要放这个宏定义即可。

```
#define TBCityIconInfoMake(text, imageSize, imageColor) [TBCityIconInfo iconInfoWithText:text size:imageSize color:imageColor]
#define kTBCityIconHomeTabMe TBCityIconInfoMake(@"\U0000e61c", 24,  HEXCOLOR(0xf4824f))
```

## 效果分析

### 体积减小效果

我们对项目的图片做了一些替换，目前替换了69张2x图，同时减少67张3x图。为了计算这些图片打包后实际所占体积，我们建立了一个空工程，通过执行Archive、Estimated App Store Size来查看体积。在工程中放入2x或3x图片后再次计算。我们通过FontForge对字体做了简化（Element -> Simplify -> Simplify）和取整（Element -> Simplify -> Round -> To Int），结果如下（单位KB）：

资源 | 空工程 | 2x图 | 3x图 | 字体
--- | --- | --- | --- | ---
工程体积 | 195 | 249 | 268 | 214
资源体积 | 0 | 54 | 73 | 19

目前看来替换这部分图片后，仅考虑2x图则替换后体积是之前的`35%`，如果算上3x图则体积是之前的`15%`！

### 生成图片的性能

我们对比了字体生成图片和直接使用PNG图片的效率。图片选择了32、64、200三种尺寸的2倍图。统计了两种方法创建1000次UIImageView的耗时，平台为iPhone 5S/iOS8。结果如下（单位：秒）：

方法\尺寸 | 32 | 64 | 200
--- | --- | --- | ---
字体生成图片 | 0.426 | 0.476 | 2.085
PNG图片 | 0.454 | 0.441 | 0.467

PNG图片加载的速度受像素大小影响很小。字体生成图片的方式在32像素的2倍图中，字体生成图片的速度甚至比加载PNG图片还要快。最坏的情况是生成1000张200像素的2倍图耗时达到了2秒多。但是这种情况比较极端，即使有多张大图展示的需求，也可以通过UITableView来做懒加载。而且平均下来每张图耗时2毫秒。总体来看字体生成图片效率还可以接受。

### 项目中应用

目前淘点点iOS插件版中的图标有半数替换为IconFont。新需求用到的图标也会优先采用IconFont。一个典型的应用IconFont的页面比如我的页面。应用每个页面都有的Tabbar的四个图标、列表中的四个彩色图标、头部的四个白色图标和导航栏的消息图标。目前已经上线，读者可以将手机淘宝最新的ipa下载解压，查看Payload/Taobao4iPhone中的文件，就会发现找不到上面提到这几个图标的图片文件。同时会看到LLIconfont.ttf文件，也就是点点使用的字体库。

![taodiandian](/images/2015-04-03-using-icon-font-in-ios-taodiandian.png)

IconFont项目已经整理开源出来：[IconFont项目]。工程中包含核心代码和Demo，核心功能最低兼容iOS5。已经放到了CocoaPods上，名称是`IconFont`。

## 其他有趣的方案

### PDF绘制矢量图

PDF也可以存储矢量图。Xcode6下新建TabViewController后，tab的图标采用的是PDF文件。我们想类似使用PDF图标。[Using Vector images in Xcode6]文章中指出，实际上Xcode6下使用PDF只是在编译时根据PDF生成不同倍数图片，并不在应用中使用矢量图。并且Asset Catalog从iOS7开始才能使用。从兼容性和缩小图片体积的考虑，这种方法没有帮助。

[UIImage-PDF]是GitHub上收获Star比较多的一个项目，实现了PDF绘制图片的功能，并且没有系统版本兼容的问题。相比与IconFont，PDF方案可以可以存储颜色信息，可以像Sprite一样从一个PDF导出多张图片。但是相比IconFont，占用体积也要大得多。另外发现AI文件直接导出PDF后体积很大，转为SVG后再转为PDF体积会减小一些。目前用一个比较复杂的矢量图转换，PDF的体积与原图的体积大致一样，因此这种方法对体积减小并无帮助。

### 字符串绘制矢量图

Charles Parnot贴出了博文[用NSString替换Photoshop](http://cocoamine.net/blog/2015/03/20/replacing-photoshop-with-nsstring/)，提供了一种用字符串来保存矢量图的方式。在一个字符的二维数组中通过特定字符的位置在图中勾勒出点、线、贝塞尔曲线等来绘制图片。有了这样的能力就能够保存字体可以保存的图形。这种方法非常新颖有趣。当然局限性也很明显，绘制图形比较困难。和IconFont方案的对比我并没有做，想象那么多图用字符表示出来我就放弃了。可以推断的是，有些图中多个图形的点可能重合，用这种方式会有问题。如果要对图中的点做精细的控制，用这种方案需要将字符数组的尺寸加到很大才可以。

## 参考项目

[IconFont项目]

[FontAwesomeKit]

[FontasticIcons]

[ios-fontawesome]

[UIImage-PDF]


## 参考资料

[IconFont制作]

[Font Awesome]

[iconfont实践]

[iconfont.cn帮助]

[在iOS中使用icon font]

[绘制字符]

[AI导出SVG的优化]

[IconFont项目]:https://github.com/JohnWong/IconFont

[TexturePacker]:https://www.codeandweb.com/texturepacker/

[Design With FontForge]:http://designwithfontforge.com/

[iconfont.cn]:http://www.iconfont.cn

[FontForge]:https://github.com/fontforge/fontforge

[FontAwesomeKit]:https://github.com/PrideChung/FontAwesomeKit

[FontasticIcons]:https://github.com/AlexDenisov/FontasticIcons

[ios-fontawesome]:https://github.com/alexdrone/ios-fontawesome

[UIImage-PDF]:https://github.com/mindbrix/UIImage-PDF

[IconFont制作]:https://www.qianduan.net/css3-icon-font-guide/

[Font Awesome]:http://fontawesome.io/

[iconfont实践]:http://mux.alimama.com/posts/401

[iconfont.cn帮助]:http://iconfont.cn/help/platform.html

[绘制字符]:http://blog.csdn.net/kmyhy/article/details/7643568

[AI导出SVG的优化]:http://www.adobe.com/inspire/2013/09/exporting-svg-illustrator.html

[Using Vector images in Xcode6]:http://martiancraft.com/blog/2014/09/vector-images-xcode6/
