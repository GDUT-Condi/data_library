#coding=utf8
import redis
#默认db=0,参数还可以设置编码，输出数据形式
r = redis.StrictRedis(host="127.0.0.1",port=6379,db=0)
r.set('foo','Bar')
print r.get('foo')

#使用连接池,减少建立和释放链接的开销
pool = reids.ConnectionPool(host='localhost',port=6379)
r = redis.StrictRedis(connect_poo=pool)
