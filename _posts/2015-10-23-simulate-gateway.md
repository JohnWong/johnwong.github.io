---
layout: post
title: 模拟网关测试流量精简
category: mobile
description: 本地搭建服务器，模拟网络请求精简后网络流量的体积。
thumb: /images/2015-10-23-simulate-gateway.png
---
支付宝钱包客户端与服务器端通信中间有一层网关，使用Tengine搭建。网关层采用gzip压缩，大大减小了网络传输的体积。在做客户端RPC流量精简过程中，一般需要服务器端配合，边修改边测试比较繁琐。本地搭建了Tengine服务器，可以实现与网关一致的压缩情况，本地就可以直接做精简测试效果，十分方便。最后再推动服务器端按照优化后的情况修改。

## 搭建Tengine

为了实现100%真实的效果，没有采用Nginx，直接使用了Tengine（[http://tengine.taobao.org/](http://tengine.taobao.org/)）。下载后解压，然后：
```
./configure --without-http_ssl_module
make
make install
```

## 调整参数

需要配置gzip打开，压缩比设置到8或9可以与网关压缩完全一致。使用配置如下：

```
http {
    include       mime.types;
    default_type  application/octet-stream;

    sendfile        on;
    
    keepalive_timeout  65;

    gzip  on;
    gzip_min_length 1k;     #设置允许压缩的页面最小字节数。
    gzip_buffers 4 16k;     #用来存储gzip的压缩结果
    gzip_http_version 1.1;  #识别HTTP协议版本
    gzip_comp_level 9;      #设置gzip的压缩比 1-9 1压缩比最小但最快 9相反
    gzip_proxied any;       #无论后端服务器的headers头返回什么信息，都无条件启用压缩
    gzip_vary on;
    gzip_types               text/xml  text/plain  text/css  application/javascript  application/x-javascript  application/rss+xml;

    server {
        listen       8080;
        server_name  localhost;

        location / {
            root   html;
            index  index.html index.htm;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   html;
        }
    }
}
```

## 服务器启停

启动nginx：

```
nginx
```

停止nginx：
```
sudo kill `cat /usr/local/nginx/logs/nginx.pid` 
```