---
layout: post
title: iOS大图加载与切割
category: Past
description: 做cocos-2d-x开发的时候了解一点iOS大图加载切割的知识。
---

cocos-2d开发的时候，了解了一些知识：

在IOS上，图片会被自动缩放到2的N次方大小。比如一张1024*1025的图片，占用的内存与一张1024*2048的图片是一致的。图片占用内存大小的计算的公式是；长*宽*4。这样一张512*512 占用的内存就是 512*512*4 = 1M。其他尺寸以此类推。（ps:IOS上支持的最大尺寸为2048*2048）。
原生SDK开发给出了贴大图的一些解决方案，包括PhotoScroll和ScrollViewSuite等代码。

切图工具[Tile-Cutter](https://github.com/jlamarche/Tile-Cutter)，还没使用。

ImageMagic切图切出来和PhotoScroll所需的图片比较类似，命令如下：

```
convert bigimage.png -crop 256x256 -set filename:tile "%[fx:page.x/256+1]_%[fx:page.y/256+1]" +repage +adjoin "tile_25_%[filename:tile].png"
```
 
需要缩放就加参数 -resize 25% 