---
layout: post
title: "HTML5 Web Audio API实现【董小姐】播放"
category: Past
description: 论坛有人发了matlab实现的董小姐，于是想在自己熟悉的领域也试试看。
---
论坛有人发了matlab实现的董小姐，于是想在自己熟悉的领域也试试看。之前用Python做过发出指定频率的声音，但是这个对第三方库的依赖较大。于是准备在JavaScript中实现。

先发一个不错的参考资料：[http://www.html5rocks.com/zh/tutorials/webaudio/intro/](http://www.html5rocks.com/zh/tutorials/webaudio/intro/)

首先需要处理Web Audio API名称的问题，并取得AudioContext的实例：

``` javascript
try {
  // Fix up for prefixing
  window.AudioContext = window.AudioContext || window.webkitAudioContext;
  context = new AudioContext();
} catch (e) {
  alert('Web Audio API is not supported in this browser. Chrome is strongly recommended!');
}
```

目前对Web Audio的支持，Chrome做的最好，Firefox正在努力，测试版已经实现，IE大家都明白，还不支持。

然后是声音的来源，我选择了MIDI.js中的钢琴声音，引入这个js文件，里面是base64编码后的钢琴各个按键的声音。对编码解码需要用到base64binary.js。用上面取得的context做音频解码。解码后回调函数中，将AudioBuffer存到数组中。这里MIDI.keyToNote是做钢琴按键到数字的转换。

``` javascript
var base64 = notes[key].split(',')[1];
var data = Base64Binary.decodeArrayBuffer(base64);
(function(note) {
  total ++;
  context.decodeAudioData(data, function(buffer) {
    MIDI.soundBuffer[type][note] = buffer;
    // trigger event;
    count ++;
    if(count == total)
      triggerEvent(document, "midi:init");
  })
})(MIDI.keyToNote[key]);

MIDI.playSound = function(note, time) {
  if(callback)
    setTimeout(callback, time * 1000);
  if(note == null || note < MIDI.pianoKeyOffset )
    return;
  var buffer = instrument[note];
  var source = context.createBufferSource(); 
  source.buffer = buffer; 
  source.connect(context.destination); 
  source.start(time);
}
```

其中context.destination指的是音频输出设备。捎带花了点时间做了歌词播放同步标记，Chrome的timer很准确啊，一首歌下来，音频播放和歌词看不出不同步。

项目代码上传到GitHub：[https://github.com/JohnWong/midi-javascript](https://github.com/JohnWong/midi-javascript)

演示地址：[http://impress.sinaapp.com/midi-javascript/missdong.html](http://impress.sinaapp.com/midi-javascript/missdong.html)