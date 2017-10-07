---
layout: post
title: "解决系统升级后 libimobiledevice 使用的问题"
category: mobile
description: 尝试对 libimobiledevice 升级
thumb: /images/2017-10-06-upgrade-libimobiledevice-in-macos-high-sierra-2.jpg
---

[https://github.com/libimobiledevice/libimobiledevice](https://github.com/libimobiledevice/libimobiledevice)这个库非常方便，对于 iOS 开发来说可以提升效率。升级到 macOS High Sierra 后发现这个库无法使用，各种命令都是无法连接到 lockdownd，比如`ERROR: Could not connect to lockdownd, error code -17`。在 issue 里搜了下也没有找到解决办法，自己尝试解决了一下。

## 在 homebrew 里升级版本

之前采用 homebrew 来安装的，尝试升级下版本。升级到1.2.0，仍然出错。希望升级到最新版head，在升级过程中报错失败。

## 手动编译

把源代码拉下来，按照README的指引尝试安装，报错`OpenSSL support explicitly requested but OpenSSL could not be found`。大概搜了下，原因是 High Sierra 把 SSL 库从 OpenSSL 0.9.8zh 切换到 LibreSSL。而且通过 homebrew 安装的 OpenSSL 也是 keg-only 的，并且禁止通过 brew link openssl 添加软链接。换条思路禁用 openssl，提示需要安装GnuTLS。用 homebrew 安装了`gnutls`和`libgcrypt`，之后再安装就没问题了。

```
brew install gnutls
brew install libgcrypt
./autogen.sh --disable-openssl
make
make install
```

安装之后尝试了下，成功了。原来更新到最新版就好了，比预期的解决难度小很多了。