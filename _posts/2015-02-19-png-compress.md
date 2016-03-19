---
layout: post
title: PNG图片极限压缩
category: showcase
description: 春节假期写代码，除夕夜总结出文章，想想也是醉了。
thumb: /images/2015-02-19-png-compress-02.png
---

之前面对应用体积压缩的问题时，找到了目前比较好的PNG压缩方法[ImageAlpha]+[ImageOptim]。这种方法一个不便之处在于[ImageAlpha]是一个单张图片处理工具，而且需要手动保存图片。图片较多时非常费力。如果有工具能够将两个工具结合到一起，提供批量处理的能力，将会很有帮助。[ImageOptim]作者也考虑过[添加有损压缩功能](https://github.com/pornel/ImageOptim/issues/17)，项目中也包含了[pngquant]，只是8个月过去了还没结果。[ImageOptim-CLI]是一个集成了这两个工具和JPEGmini的命令行工具，利用AppleScript实现对图形界面程序的操纵。用起来发现有时候会出现大图未被压缩的问题，同时命令行的交互相比图形界面在易用性上还是有差距。因此我花了些时间将[ImageAlpha]的有损压缩功能集成到[ImageOptim]中，可以对PNG图片实现微小失真下高压缩率。并且利用[ImageOptim-CLI]的对比方法比较了这些工具的压缩效率。

### ImageAlpha

![ImageAlpha Screenshot](//dn-johnwong.qbox.me/images/2015-02-19-png-compress-01.png)

[ImageAlpha]是一个Mac OS X下的图形化有损图片压缩工具，内置了[pngquant]，[pngnq-s9]，Blurizer和[posterizer]四种压缩工具。这些工具减少PNG文件大小并保留透明度通道。ImageAlpha采用PyObjC编写，但是作者对这种方式已经累觉不爱。使用一段时间后的经验是内置的几种压缩工具看起来[pngquant]最有效的，压缩时颜色数采用256可以在难以分辨出质量损失的情况下大幅压缩图片体积。虽然对于颜色数较少的图片可以通过减少颜色数来进一步压缩体积，但这种方式依赖人工并不能实现自动化。

[pngquant](http://pngquant.org/)将24位或32位的RGBA PNG图转换成8位PNG图并保留透明度通道。这样得到的图兼容所有的现代浏览器，并且可以通过一个兼容性设置在IE6上实现较好的降级。优化后文件相比24/32位通常可以缩小40-70%的体积。

### ImageOptim

![ImageOptim Screenshot](//dn-johnwong.qbox.me/images/2015-02-19-png-compress-02.png)

[ImageOptim]是一款非常优秀的无损图片压缩工具，相信大多数iOS开发者都知道它。它通过优化压缩参数，移除无用的文件元数据和不必要的颜色配置来实现图片的无损压缩。它集成了最好的压缩工具，包括[PNGOUT]，[Zopfli], [Pngcrush], [AdvPNG]，[OptiPNG]，[JpegOptim]，[JPEGrescan]，[Jpegtran]和[Gifsicle]。除了压缩效率高，它还支持[命令行](https://imageoptim.com/command-line.html)、充分利用多核、批量处理和拖拽操作方式。

关于其算法可以参考项目的[issue讨论](https://github.com/pornel/ImageOptim/issues/79)。基本方法是利用用多个工具压缩图片，选取体积最小的替换原图。如果所有方法压缩后变大则保留原图（比如已经被其压缩过一次的图片可能再压变大）。作者期望压缩算法按照一定顺序进行，前一次如果压缩有效，后一次基于前一次的压缩结果进行。实际情况下几种工具大多基于原图进行压缩，这可能是一个值得以后改进的地方。

### ImageOptim with pngquant

[ImageOptim with pngquant]是我对[ImageOptim]改进加入[pngquant]的版本。对项目的改动包括：

- 对pngcrush版本降级来避免编译错误。
- 设置页面和菜单加入pngquant复选框，可以选择开启或关闭pngquant。
- 处理图片时，如果pngquant工具勾选，则先使用pngquant预处理。

你可以自行编译或者下载[编译好的应用](https://github.com/JohnWong/ImageOptim/releases/download/1.5.4/ImageOptim-with-pngquant.zip)

需要注意的是压缩之前做好版本控制或者备份，因为压缩是有损的并且会修改原文件，可能会变得失真严重。所以我一般是在把版本控制下的项目里的图片拖进工具，提交之前在SourceTree中预览一下压缩前后的图片，以防失真严重。虽然目前为止这样的压缩都几乎不会感受到品质的损失，但是还是小心为上。另外用ImageOptim压缩有个特点，就是压缩之后再次压缩体积可能反而变大，所以如果做iOS开发，需要将Xcode编译设置中的PNG压缩关掉，可以参考[ImageOptim上关于Xcode的文章](https://imageoptim.com/xcode.html)。另外如果要在IE下使用，那么需要修改运行[pngquant]的参数。如果有同学遇到这样的需求请联系我，我再来支持这个功能。

### 压缩工具对比

[ImageOptim-CLI]项目的`gh-pages`分支里面提供了测试压缩工具效果的方法。需要注意的是失真的计算依赖于[ImageMagick](http://www.imagemagick.org/)，需要先安装它。 对于几种压缩工具的对比参见[http://jamiemason.github.io/ImageOptim-CLI/](http://jamiemason.github.io/ImageOptim-CLI/)。

工具对比的使用方法参加项目的README。我对项目做了一些修改，添加了我改进的[ImageOptim with pngquant]和宗心制作的ImageOptim两项。结果参见[压缩工具PNG图对比结果](http://johnwong.github.io/ImageOptim-CLI/comparison/png/photoshop/desc/)。作者列出的`ImageAlpha & ImageOptim`、宗心的版本和我改进版本原理一致，都是使用pngquant预处理，可能由于参数或者压缩算法版本不同导致结果不尽相同。我改进版本对于图片压缩稍稍领先。


### Next

- PNG压缩目前没有更好的方法了，有空的时候研究一下WebP，看看能不能让图片体积变得更小。
- [jpeg-archive]是JPEGmini的一个免费替代品，尝试加入它来压缩JPEG图片。

### Further Reading

#### [PNG that works]

介绍了PNG的几种类型、浏览器兼容性和一些工具，总结下来：

* PNG在IE4后可用，使用GIF是在浪费带宽。
* 使用256色的PNG。
* 避免使用24位PNG，pngquant可以帮到你。
* 使用一个PNG优化器来得到更小的文件并避免陷阱。

#### [Lossy PNG]

如果对PNG的有损压缩感兴趣，那么可以阅读[Lossy PNG]一文。这篇文章介绍了有损PNG的原理。作为无损图片格式创造出来的PNG图片可以通过Lossy averaging filter，PNG8和Posterization实现有损压缩。PNG相比JPEG是否更小取决于图片。JPEG通常体积更小，除了有尖锐边缘（比如文本）或者包含透明度（JPEG不支持）的图片。优化后的有损PNG仍然比有损的JPEG-XR/WebP/JPEG-2K大一点，但优势在于可以被所有浏览器和操作系统支持。

#### [Kornel Lesiński]
最后膜拜一下[Kornel Lesiński]，上面提到的几篇文章和工具[ImageAlpha]、[ImageOptim]、[pngquant]等都是他的作品。

#### Homepage

[ImageOptim with pngquant]

[编译好的应用]可供下载。

#### Stastics

`2015-02-16` ~ `2015-02-19`

共计4个commit。

[ImageAlpha]:https://github.com/pornel/ImageAlpha
[ImageOptim]:https://github.com/pornel/ImageOptim
[pngquant]:http://pngquant.org
[pngnq-s9]:http://sourceforge.net/projects/pngnqs9/
[posterizer]:https://github.com/pornel/mediancut-posterizer
[PNGOut]:http://www.advsys.net/ken/util/pngout.htm
[ImageOptim-CLI]:https://github.com/JamieMason/ImageOptim-CLI
[PNG that works]:http://calendar.perfplanet.com/2010/png-that-works/
[Lossy PNG]:http://pngmini.com/lossypng.html
[Zopfli]:http://googledevelopers.blogspot.co.uk/2013/02/compress-data-more-densely-with-zopfli.html
[Pngcrush]:http://pmt.sourceforge.net/pngcrush/
[AdvPNG]:http://advancemame.sourceforge.net/doc-advpng.html
[OptiPNG]:http://optipng.sourceforge.net/
[JpegOptim]:http://www.kokkonen.net/tjko/projects.html
[JPEGrescan]:https://github.com/kud/jpegrescan
[Jpegtran]:http://jpegclub.org/jpegtran/
[Gifsicle]:http://www.lcdf.org/gifsicle/
[jpeg-archive]:https://github.com/danielgtaylor/jpeg-archive
[Kornel Lesiński]:https://github.com/pornel/
[ImageOptim with pngquant]:https://github.com/JohnWong/imageoptim
[编译好的应用]:https://github.com/JohnWong/ImageOptim/releases/tag/1.5.4