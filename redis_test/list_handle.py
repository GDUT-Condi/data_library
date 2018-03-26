#coding=utf8
LPUSH key value [value ...]#在头部插入数据
RPUSH key value [value ...]#在尾部插入数据
LINSERT key BEFORE|AFTER pivot value #在一个元素前|后插入新数据
LSET Key index value #基于索引0的下标设置元素值
L/RPOP 移除key对应list #第一个或最后一个元素
LRANGE Key start stop #返回存储在key列表基于索引的元素
LTRIM key strat stop #裁剪列表，start >stop删除key
LLEN key #返回列表长度
LINDEX key index #返回列表里索引对应的元素
