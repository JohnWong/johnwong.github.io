---
layout: post
title: "jQuery上传文件大小校验"
category: Past
description: 为jQuery的Validator增加一个filesize方法，在前端校验文件大小。
---
jQuery的Validator增加一个filesize方法。为了在IE下可以使用前端校验，需要判断浏览器类型。如果是IE需要使用ActiveX来校验。客户端需要修改IE设置才能运行，具体为：
```
IE -> Internet选项 -> 安全 -> 自定义级别 -> ActiveX控件和插件 -> 对未标记为可安全执行脚本的ActiveX控件初始化并执行脚本（不安全） -> 启用
```

不得不说，如果没有IE将会是多么美好的世界，减少好多兼容性问题


```javascript
$.validator.addMethod('filesize', function(value, element, param) {
    var size;
	if($.browser.msie){
		var myFSO = new ActiveXObject("Scripting.FileSystemObject");
		 var filepath = value;
		 var thefile = myFSO.getFile(filepath);
		 size = thefile.size;
	} else {
		size = element.files[0].size;
	}
    return this.optional(element) || (size <= param);
});
```