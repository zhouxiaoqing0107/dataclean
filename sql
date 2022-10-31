#返回时间戳
unix_timestamp('20210819','yyyymmdd')

#sql从时间戳返回yyyy-mm-dd格式的时间
from_unixtime('1610899680','yyyy-mm-dd')

#建表
drop table if exists test;
create table test
(id string,
 dat string)
partitioned by (days string)

#插入数据
insert into table_1 values (1,2)

insert into table_1 partition (days=1) values(1,2)