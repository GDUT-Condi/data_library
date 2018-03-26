#coding=utf8
#hash用于存储对象，对象的格式为键值对
HSET key field value #设置单个属性
HMSET key field value [field value ...] #设置多个属性
HGET key field #获取一个属性的值
HMGET key field[field ...]#获取多个属性的值
HGETALL key #获取所以属性和值
HKEYS key #获取所有属性
HLEN Key #获取包含属性的个数
HVALS key #获取所有值
HEXISTS key field #判断属性是否存在
HDEL key field [field ...] #删除属性和值
HSTRLEN key field #返回值的字符串长度
