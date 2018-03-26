#coding=utf8
db.集合名称.find({条件文档})
db.集合名称.findOne({条件文档})
db.集合名称.find({条件文档}).pretty()#方法pretty()：将结果格式化
db.stu.find({age:{$gte:18}}) #加比较运算符条件
db.stu.find({$or:[{age:{$gt:18}},{gender:1}]})#逻辑运算符
db.stu.find({$or:[{age:{$gte:18}},{gender:1}],name:'gj'})#and or一起用
db.stu.find({age:{$in:[18,28]}}) #范围运算符
db.stu.find({name:{$regex:'^黄'}}})#$regex 编写正则表达式
db.stu.find({$where:function(){return this.age>20}})#使用$where后面写一个函数，返回满足条件的数据

#limit和skip
db.集合名称.find().limit(NUMBER)    
db.集合名称.find().skip(NUMBER)#方法skip()：用于跳过指定数量的文档
for(i=0;i<15;i++){db.t1.insert({_id:i})} #创建数据集
db.stu.find().skip(5).limit(4) #查询第5至8条数据

#投影：即显示某些字段
db.stu.find({},{name:1,gender:1})
#排序
db.集合名称.find().sort({字段:1,...})#参数1为升序排列,参数-1为降序排列
#统计个数
db.集合名称.find({条件}).count()
#消除重复
db.集合名称.distinct('去重字段',{条件})
