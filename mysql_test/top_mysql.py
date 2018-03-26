#coding=utf8
select students.sname,subjects.stitle,scores.score
from scores
inner join students on scores.stuid=students.id
inner join subjects on scores.subid=subjects.id;
表A inner join 表B：表A与表B匹配的行会出现在结果中
表A left join 表B：表A与表B匹配的行会出现在结果中，外加表A中独有的数据，未对应的数据使用null填充
表A right join 表B：表A与表B匹配的行会出现在结果中，外加表B中独有的数据，未对应的数据使用null填充

子查询
select sname,
(select sco.score from scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='语文' and stuid=stu.id) as 语文,
(select sco.score from  scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='数学' and stuid=stu.id) as 数学,
(select sco.score from  scores sco inner join subjects sub on sco.subid=sub.id where sub.stitle='英语' and stuid=stu.id) as 英语
from students stu;

内置函数函数
select char(97);round(1.6);rand();PI();

视图用于查询
create view stuscore as 
select students.*,scores.score from scores
inner join students on scores.stuid=students.id;
select * from stuscore;

事务
开启begin;
提交commit;
回滚rollback;
