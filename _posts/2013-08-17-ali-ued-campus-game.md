---
layout: post
title: "阿里智勇大闯关通关方法"
category: past
description: 通关阿里前端校招的游戏。
---
公布了答案可能就没意思了，本来想等结束了再贴。后来看别人贴了也就贴出来了。网址：`http://ued.campus.alibaba.com/quiz3/`（已失效）

#### 第一关：

直接源代码搜页面跳转，然后手动执行跳转过程

``` javascript
d = document.getElementById("page");
code = d.getAttribute("data-t");
window.location=Base64.decode(code);
```

#### 第二关：

移动镜子直到光线照射到两个点。这个有意思，果断保存网页，以后没事了拿来玩，做个小游戏。

``` javascript
ma = document.getElementById("ma");
mb = document.getElementById("mb"); 
ma.style.webkitTransform="rotate(-67.5deg)"; 
ma.style.top = "550px";
ma.style.left = "830px"; 
mb.style.webkitTransform="rotate(180deg)";
mb.style.left="630px";
mb.style.top="335px";
```

#### 第三关：

用canvas绘制二维码

``` javascript
con = document.getElementById('qr-canvas').getContext('2d'); 
c= //网页中注释掉的一长串数字
d = c.split(" "); 
for(var e in d){ console.log(d[e]); 
  f = d[e].split(","); console.log(f); 
  con.fillRect(Number(f[0]),Number(f[1]),Number(f[2]),Number(f[3])); 
}
```

#### 第四关：

第一次人肉通过，结果最后一关没在规定时间内做完，然后写代码记录信息。也可以通过user script或者chrome extension来自动将js载入到页面，懒得做，就把这段js保存到书签中，每次打开新页面就点击一下。最后去localStorage找信息。

``` javascript
var m = document.getElementById("message");
if(!localStorage.msg)
  localStorage.msg = "";
localStorage.msg += m.innerHTML;
var next = document.getElementById("next-room");
var url = window.location.href;
url = url.replace(/room=.*$/, "room=" + next.innerHTML);
window.location = url;
```

#### 第五关：

真的是拼人品。有一次轻松猜对，有一次搜索也查不出来。

#### 第六关：

和第一关类似。

``` javascript
d = document.getElementById("page");
code = d.getAttribute("data-p");
window.location=Base64.decode(code);
```

然后第二天收到了miss-x的邮件。周末改改简历再投吧，之前的简历写的太烂了。