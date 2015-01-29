---
layout: post
title: "看书发现IE的大坑"
category: Past
description: 今天看Dojo权威指南，里面提到了IE的一个大坑。
---
今天看dojo权威指南，里面提到了IE的一个大坑：

一个网页，内容如下：

``` html
<form name="foo">
form
</form>
<div id="foo">
div
</div>然后执行一段js代码document.getElementById("foo").innerHTMLchrome下得到的是div

<form name="foo">
form
</form>
<div id="foo">
div
</div>
```

`document.getElementById("foo").innerHTML`在IE下得到的是form!!!!!!

WTF 据说IE的id和name属性是合并在一起的





