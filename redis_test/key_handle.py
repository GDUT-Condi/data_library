#coding=utf8
KEYS pattern #查找键，支持正则
EXISTS key [key ....]#判断键存在则返回1否则返回0
TYPE key #查看value类型
DEL key #删除对应键值对
expire key secondes #设置过期时间(s)
TTL key #查看有效时间(s)
