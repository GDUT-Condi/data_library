#coding=utf8
db.集合名称.insert(document)
db.集合名称.update(
           <query>,
              <update>,
                 {multi: <boolean>}
                 )
db.stu.update({name:'hr'},{name:'mnc'})#全文档更新
db.stu.update({name:'hr'},{$set:{name:'hys'}}) #指定属性更新，通过操作符$set
db.stu.update({},{$set:{gender:0}},{multi:true})#修改多条匹配到的数据
db.集合名称.save(document)#已经存在则修改，如果不存在则添加
db.stu.remove({gender:0},{justOne:true})#前一个为删除条件
db.stu.remove({gender:0},{justOne:true})
db.stu.remove({}) #全部删除
db.createCollection('sub',{capped:true,size:10})#设置集合大小，超出则覆盖

