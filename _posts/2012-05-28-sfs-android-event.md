---
layout: post
title: "SFS&Android——SFS客户端全部事件详细"
category: past
description: 读研前实习用了下SFS。
---
SFS是smartfoxserver的缩写。最近公司的一个Android项目要求使用SFS作为服务器。我去，服务器开发目前就我自己在研究。他们也真是放心。因为这个服务器是针对Flash开发的，官网上说支持Android，但是相关资料几乎没有。首先从学习SFS的Java客户端开始学习。



首先需要安装SFS，然后使用其中的API。SFS有pro和2x两个适合的版本，2x是新版，但是暂且用pro了。去官网可以下载JavaSE和Android的例程。Java的例程导入Eclipse需要使用File->new->other，选择Java project from from existing ant buildfile。其中需要使用loadConfig方法载入xml配置文件。xml文件路径可能有错误，使用的是程序的默认用户路径，可以通过程序中打印用户路径来找到这个路径拷入配置文件。

使用API主要用到了SmartFoxClient这个类。在程序中对其事件进行相应即可。还是要小小激动一下，毕业设计做的五子棋服务器端没有参考资料，凭经验琢磨出来了一套消息机制。没想到基本的消息流程跟SFS还是比较一致的。这里列出所有事件：

sfs = new SmartFox();



//接收服务器超管信息事件



sfs.addEventListener(SFSEvent.ADMIN_MESSAGE, listener);



//接收加载配置文件失败事件



sfs.addEventListener(SFSEvent.CONFIG_LOAD_FAILURE, listener);



//接收加载配置文件成功事件



sfs.addEventListener(SFSEvent.CONFIG_LOAD_SUCCESS, listener);



//接收连接服务器成功事件



sfs.addEventListener(SFSEvent.CONNECTION, listener);



//接收连接服务器失败事件



sfs.addEventListener(SFSEvent.CONNECTION_LOST, listener);



//接收连接服务器恢复事件



sfs.addEventListener(SFSEvent.CONNECTION_RESUME, listener);



//接收重试服务器连接事件



sfs.addEventListener(SFSEvent.CONNECTION_RETRY, listener);



//接收响应后台扩展事件



sfs.addEventListener(SFSEvent.EXTENSION_RESPONSE, listener);



//接收用户邀请事件



sfs.addEventListener(SFSEvent.INVITATION, listener);



//接收用户邀请事件



sfs.addEventListener(SFSEvent.INVITATION_REPLY, listener);



//接收被邀请用户的回复事件



sfs.addEventListener(SFSEvent.INVITATION_REPLY_ERROR, listener);



//接收用户登陆区域事件



sfs.addEventListener(SFSEvent.LOGIN, listener);



//接收用户登区错误事件



sfs.addEventListener(SFSEvent.LOGIN_ERROR, listener);



//接收用户登出区域事件



sfs.addEventListener(SFSEvent.LOGOUT, listener);



//接收用户登出区域事件



sfs.addEventListener(SFSEvent.MODERATOR_MESSAGE, listener);



//接收领头者消息事件



sfs.addEventListener(SFSEvent.OBJECT_MESSAGE, listener);



//接收游戏者成功转换为观察者事件



sfs.addEventListener(SFSEvent.PLAYER_TO_SPECTATOR, listener);



//接收游戏者转换为观察者错误事件



sfs.addEventListener(SFSEvent.PLAYER_TO_SPECTATOR_ERROR, listener);



//接收私人消息事件



sfs.addEventListener(SFSEvent.PRIVATE_MESSAGE, listener);



//接收公共消息事件



sfs.addEventListener(SFSEvent.PUBLIC_MESSAGE, listener);



//接收创建房间事件



sfs.addEventListener(SFSEvent.ROOM_ADD, listener);



//接收房间基础属性改变事件



sfs.addEventListener(SFSEvent.ROOM_CAPACITY_CHANGE, listener);



//接收房间基础属性改变错误事件



sfs.addEventListener(SFSEvent.ROOM_CAPACITY_CHANGE_ERROR, listener);



//接收查找房间的信息结果事件



sfs.addEventListener(SFSEvent.ROOM_FIND_RESULT, listener);



//接收订阅一个房间组事件



sfs.addEventListener(SFSEvent.ROOM_GROUP_SUBSCRIBE, listener);



//接收订阅一个房间组错误事件



sfs.addEventListener(SFSEvent.ROOM_GROUP_SUBSCRIBE_ERROR, listener);



//接收创建房间错误事件



sfs.addEventListener(SFSEvent.ROOM_CREATION_ERROR, listener);



//接收取消已订阅的一个房间组事件



sfs.addEventListener(SFSEvent.ROOM_GROUP_UNSUBSCRIBE, listener);



//接收取消已订阅的一个房间组错误事件



sfs.addEventListener(SFSEvent.ROOM_GROUP_UNSUBSCRIBE_ERROR, listener);



//接收进入房间事件



sfs.addEventListener(SFSEvent.ROOM_JOIN, listener);



//接收进入房间错误事件



sfs.addEventListener(SFSEvent.ROOM_JOIN_ERROR, listener);



//接收房间名更改事件



sfs.addEventListener(SFSEvent.ROOM_NAME_CHANGE, listener);



//接收房间名更改错误事件



sfs.addEventListener(SFSEvent.ROOM_NAME_CHANGE_ERROR, listener);



//接收房间密码更改事件



sfs.addEventListener(SFSEvent.ROOM_PASSWORD_STATE_CHANGE, listener);



//接收房间密码更改错误事件



sfs.addEventListener(SFSEvent.ROOM_PASSWORD_STATE_CHANGE_ERROR, listener);

