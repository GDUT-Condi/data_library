#coding=utf8
sadd key member [member ...]#添加元素
smembers key #获取key集合所有的元素
scard key #返回集合元素个数
sinter key [key ]#求多个集合的交集
sdiff key [key ...] #求某集合与其它集合的差集
SUNION key [key ...] #求多个集合的合集
SISMEMBER key member #判断元素是否在集合中 

zset#每个元素都会关联一个double类型的score，表示权重，通过权重将元素从小到大排序
ZADD key score member [score member ...] #添加
ZRANGE key start stop #返回指定范围内的元素
ZCARD key #返回元素个数
ZCOUNT key min max #返回有序集key中，score值在min和max之间的成员
ZSCORE key member #返回有序集key中，成员member的score值
