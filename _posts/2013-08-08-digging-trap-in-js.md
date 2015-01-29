---
layout: post
title: "开始挖掘js与dojo可能踩的坑"
category: Past
description: 开始研究Dojo，开了个头但是中止了。
---
1. && 与 || 操作符

如果&&左侧表达式的值为真值，则返回右侧表达式的值；否则返回左侧表达式的值。

如果||左侧表达式的值为真值，则返回左侧表达式的值；否则返回右侧表达式的值。

所以不要天真地以为他们始终返回boolean

``` javascript
"abc" && "123"  // "123"
"" && "123"  // ""2. 上一个坑看起来dojo 1.x踩了

"abc" && "123"  // "123"
"" && "123"  // ""
```


dojo.isAlien判断是否是build-in function.&nbsp;

``` javascript
// summary:
//		Returns true if it is a built-in function or some other kind of
//		oddball that *should* report as a function but doesn't
return it && !d.isFunction(it) && /\{\s*\[native code\]\s*\}/.test(String(it)); // Boolean

// summary:
//		Returns true if it is a built-in function or some other kind of
//		oddball that *should* report as a function but doesn't
return it && !d.isFunction(it) && /\{\s*\[native code\]\s*\}/.test(String(it)); // Boolean
```

一些例子。

``` javascript
dojo.isAlien("") // ""
dojo.isAlien(0) // 0

dojo.isAlien(alert) // false
dojo.isAlien(isFinite) // false类&#20284;的类型判断还有一些不太严谨的地方。估计是dojo自己也发现这里坑比较大，这个方法以及其他一些类型判断在2.0后移除了。

dojo.isAlien(alert) // false
dojo.isAlien(isFinite) // false
```

[http://dojotoolkit.org/reference-guide/1.9/releasenotes/migration-2.0.html#testing-object-types](http://dojotoolkit.org/reference-guide/1.9/releasenotes/migration-2.0.html#testing-object-types)



