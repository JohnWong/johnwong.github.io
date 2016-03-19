---
layout: post
title: "jQuery UI在Server 2008 IE8下DatePicker问题修复"
category: past
description: jQuery UI的DatePicker在Server 2008的IE8下出现问题。
---
这真是个WTF的问题，类似参见[Stack Overflow](http://stackoverflow.com/questions/5454489/jquery-datepicker-having-trouble-in-ie8)

这个DatePicker问题只在Server 2008的IE8下出现。至于为什么win7的IE8支持，Server2008的IE8不支持，就不知道了。可能升级jQuery UI版本能够升级这个问题，但是由于实验室项目比较庞大，升级代价太大。所以只能试图修复。

1. Debug一段时间，发现问题究其根本是由于button、a、td标签的onclick方法不被IE8支持。
2. 现在实用的jQuery UI版本是min版，看着真是费劲，从网上下载来源码，看着舒服多了。
3. 修改jQuery源代码。7894行：

```javascript
_selectDay: function(id, month, year, td) {  
    var target = $(id);  
    if ($(td).hasClass(this._unselectableClass) || this._isDisabledDatepicker(target[0])) {  
        return;  
    }  
    var inst = this._getInst(target[0]);  
    inst.selectedDay = inst.currentDay = $('a', td).html(); 
``` 

修改为

```javascript
_selectDay: function(id, month, year, day) {  
    var target = $(id);  
    if (this._isDisabledDatepicker(target[0])) {  
        return;  
    }  
    var inst = this._getInst(target[0]);  
    inst.selectedDay = inst.currentDay = day; 
```

8445行和8454行将响应方法由onclick转移到href。8462-8467行的button标签修改为a标签。同样将响应方法从onclick转移到href。这两个button修改标签之后样式不和谐，加入了一些css来控制与之前一致。

```css
float: right;
margin: 0.5e m 0.2e m 0.4e m;
padding: 0.2e m 0.6e m 0.3e m 0.6e m;
color: #2f6ca9;
font-size: 0.8em;
font-weight: bold;
text-align: center;
text-decoration: none;
```

最烦浏览器兼容性问题，这次又成功解决了。