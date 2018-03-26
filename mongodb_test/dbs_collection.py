#coding=utf8
#数据库操作
db当前数据库
show dbs 所有数据库名称
use dbname 切换数据库
db.dropDatabase() 删除当前指向的数据库

#集合操作
db.createCollection(name,options) 集合创建，options指定集合的配置如大小
show collections 查看当前数据库的集合
db.集合name.drop() 删除集合
