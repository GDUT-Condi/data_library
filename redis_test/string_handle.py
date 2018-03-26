#coding=utf8
#set(name,value,ex=None,px=None,nx=False,xx=False)
#ex,px过期时间(秒，毫秒)，nx为True当name不存在，当前set操作执行，xx为True时与nx相反
setnx(name,value),当name不存在，执行设置添加操作
#还有setex,psetex
mset(*args,**kwargs)
mset(k1='v1',k2='v2')或mset({'k1':'v1','k2':'v2'})
get(name)
mget(keys,*args)
#设置新值并获取原来的值
getset(name,value)

#在redis-cli中操作
INCR/DECR key #key 对应value加/减1
INCRBY/DECRBY key increment #将key对应value加/减整数
APPEND key value #追加值
STRLEN key #获取值长度
