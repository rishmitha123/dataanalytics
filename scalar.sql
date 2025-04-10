
use dataanalytics;

-- Scalar function operates on single value and returns a single value


select UCASE ("Hello World!") as UpperCase_String;
select LCASE ("Hello World!") as LowerCase_String;
select substring("Hello World!",4,8) as sub_String;
select MID("Hello World!",4,8) as subString;
select Length ("Hello World!") as String_length;
select ROUND(1560.23455,2) as Round_value;

select * from products;
select ROUND(price) as Round_value from products;
select * from orders;


create table user(userid int auto_increment,name varchar(50),
primary key(userid));
alter table user auto_increment=101;
insert into user(name) values("radha"),("gopi"),("ramesh");
select * from user;

-- CREATE SEQUENCE example_01
--  as int 
--  start with 10
--  increment by 10;

create table doctor(doctorid int,doctorname varchar(255));
insert into doctor values(1,null),(2,"ajay"),(3,"gokul"),(4,null);
select * from doctor;
select *,coalesce(doctorname,'kohli')as doc from doctor;