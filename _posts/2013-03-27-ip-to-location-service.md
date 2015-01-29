---
layout: post
title: "一个IP地址搜索服务"
category: Past
description: 今天偶然发现了有道的ip地址搜索服务
---

今天偶然发现了有道德ip地址搜索服务，网址是：

[http://www.youdao.com/smartresult-xml/search.s?type=ip&q=10.213.28.0](http://www.youdao.com/smartresult-xml/search.s?type=ip&q=10.213.28.0)

这个页面在我这里返回的结果是对方和您在同一个局域网内。以前能判断到时哪栋教学楼或者宿舍楼，现在学校网络改造后就只判断到同一个局域网，不能精确到教学楼宿舍楼了。

该服务已经无法使用。幸亏自己做的论坛显IP的插件没有使用这个服务。用了自己做的ip地址转换服务，pos=1时解析北邮内网ip。


[http://pytool.sinaapp.com/geo?ip=10.108.1.1&pos=1](http://pytool.sinaapp.com/geo?ip=10.108.1.1&pos=1)

源代码: [https://github.com/JohnWong/python-tool](https://github.com/JohnWong/python-tool)

