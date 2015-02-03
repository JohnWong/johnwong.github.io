---
layout: post
title: Geoguessr游戏破解
category: Past
description: 没人比我分高哈哈。
thumb: /images/2014-02-11-hack-geoguessr.jpg
---
[Geoguessr](http://geoguessr.com/)是一个好玩的根据街景猜位置的游戏。建议先玩玩，充分体会游戏的乐趣。学会了破解的方法就没意思了。接下来进入破解方法。需要Chrome浏览器和Web调试的一点知识。
 
![geoguessr](/images/2014-02-11-hack-geoguessr.jpg)

#### 1. 捕捉街景的网络交互。
按F12打开调试工具。刷新网站，加载完成后在network选项卡下凭借缩略图能够很快找到街景的网络请求。我这里找到的是`https://cbks0.googleapis.com/cbk?output=tile&cb_client=apiv3&v=4&zoom=4&x=4&y=3&panoid=GUkoc-YOhxYusUlRmRiuvw&fover=2&onerr=3`。其中的参数panoid让我想起了单词panorama，这个就是街景的id。

![geoguessr](/images/2014-02-11-hack-geoguessr2.png)

#### 2. 街景id转成经纬度。
Google街景的地址的格式是`http://maps.google.com/?hl=en&ie=UTF8&ll=42.843751,-68.203125&spn=0,313.461914&z=5&layer=c&cbll=41.916553,-75.883875&panoid=zRjnm1iOEUZN_ueQbq6MlQ&cbp=12,278.28,,0,6.02`，把这里的panoid换成刚才得到的街景id。我使用的是新版Google Maps，地址格式是`https://www.google.com/maps/preview/@47.528448,-92.168024,3a,75y,294.09h,71.36t/data=!3m4!1e1!3m2!1sGUkoc-YOhxYusUlRmRiuvw!2e0?hl=en`，街景id是!1s与!2e之间的部分。打开替换街景id后的链接，就能在地址中找到经纬度47.528448,-92.168024。


#### 3. 控制地图中心。
这是可以收到能够拖动地图中心到找到的经纬度。也可以用代码注入的方法控制地图拖动缩放。Google Maps API新建地图的语句是new google.maps.Map。搜索代码功能以前是在调试工具的Resources选项卡下，现在变成了按Esc调出drawer，选中search选项卡搜索。搜到了三处，都在geoguessr.js中。从名字来看，guessMapView这个变量最可能是猜结果的地图。在控制台的变量中找不到这个实例，应该是包在函数中了，就通过断点注入来插入代码。在sources选项卡中找到这个变量定义的地方，可以点击尖括号图标来让Chrome帮你完成代码格式化方便阅读。找一个能访问资源的功能，例如showHelp定义的地方打断点。点击界面的帮助按钮，就会停在断点处。之前记得先在猜的地图上把红色的标记点出来。

![geoguessr](/images/2014-02-11-hack-geoguessr3.png)

控制台输入代码：

```javascript
c = new google.maps.LatLng(47.528448,-92.168024)
this.guessMapView.map.setCenter(c)
this.guessMapView.guessMarker.setPosition(c)
```
继续执行脚本。回到页面点Make Guess就通关了，得到用于炫耀的链接哈哈。`http://url.geoguessr.com/6nYg`

不得不说猜到中国的时候坑比较大啊，因为众所周知的国内地图被要求加一个偏差。其中有一关街景是在湖边的路上，答案要点在湖里面。