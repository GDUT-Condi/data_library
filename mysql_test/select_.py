#coding=utf8
select * from 表名;
select distinct gender from students;
select * from 表名 where 条件;
select avg(id) from students where isdelete=0 and gender=0; #count,max,min,sum
select 列1,列2,聚合... from 表名 group by 列1,列2,列3... #分组后的数据筛选 having 列1,...聚合...
select * from 表名 order by 列1 asc|desc,列2 asc|desc,...
select * from 表名 limit start,count #获取部分行
执行顺序为：
from 表名
where ....
group by ...
select distinct *
having ...
order by ...
limit star,count