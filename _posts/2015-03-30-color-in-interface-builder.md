---
layout: post
title: "IB中颜色值的坑"
category: Mobile
description: 最近看到的文章终于解答了心中的疑惑
thumb: /images/2015-03-30-color-in-interface-builder.png
---

之前练手的时候用了下story board，快速开发的神器。可是在IB中设置颜色遇到了一些问题，设置的RGB值在运行时明显感觉到变掉了。

![Screen shot](/images/2015-03-30-color-in-interface-builder-1.jpg)

这也太明显了吧！用Reveal调试也证实了变化。navigation bar的title明明用的是#E007AFF，运行时变成了#0A60FF。[Stack Overflow]告诉我们这是由于IB使用了sRGB，而代码中UIColor生成采用的是G-RGB。好吧，老子忍了，手动改一下。默默地打开取色器，调整颜色配置到Generic RGB。

![Screen shot](/images/2015-03-30-color-in-interface-builder-2.jpg)

下面的十六进制颜色果然变掉了。然后在HEX COLOR那里E007AFF，运行，静静地等待奇迹发生。颜色又错了，配置变回了sRGB，逗我呢。。。试了几遍，发现只能改成G-RGB颜色配置后拖动滑动条来修改颜色，而不能输入十六进制值修改。

后来我找到了[Xcode Color Fixer]，用命令行做颜色替换。看了下代码，用PHP来做的，感觉怪怪的。。。

再后来找到了[replace srgb to calibratedRGB]，命令行一句话解决，就它了！

```bash
find . \( -name "*.xib" -or -name "*.storyboard" \) -print0 | xargs -0 sed -i '' -e 's/colorSpace="custom" customColorSpace="sRGB"/colorSpace="calibratedRGB"/g'
```

[Stack Overflow]:http://stackoverflow.com/questions/7488378/weird-colors-in-xcode-interface-builder
[Xcode Color Fixer]:https://github.com/duowan/XCode-Color-Fixer
[replace srgb to calibratedRGB]:https://www.snip2code.com/Snippet/343014/replace-srgb-to-calibratedRGB