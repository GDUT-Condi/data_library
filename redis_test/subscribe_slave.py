#coding=utf
#发布订阅
#订阅频道名称
SUBSCRIBE 频道名称 [频道名称 ...]
#取消订阅,如果不写参数，表示取消所有订阅
UNSUBSCRIBE 频道名称 [频道名称 ...]
#发布
PUBLISH 频道 消息

#主从配置
#主:bind .....
#从:bind .... 
#    slaveof 主ip port
此时主写数据 从可以获得数据
