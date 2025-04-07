create database dataanalytics;
use dataanalytics;
create table persons(
personid int,
firstname varchar(255),
lastname varchar(255),
address varchar(255),
city varchar(255));

insert into persons values( 1,"rishmitha","vankadaru","1-55 near to union bank","nuzvid");

insert into persons values(2,"rithu","varma","1-22 apartment","vijayawada"),(23,"giri","kanigolla","455 gokul theatre","eluru");

select * from persons;
delete from persons where personid=23;
update persons set firstname="junnu" where personid=1;
select * from persons;

create table users(
userid int auto_increment primary key,
username varchar(255) unique not null,
email varchar(255)unique not null,
passwordHash varchar(255) not null,
firstname varchar(50),
lastname varchar(50),
dateOfBirth date,
createdAt datetime default current_timestamp, 
lastLogin datetime,
status enum('active','inactive','suspended') default 'active',
index(email)); -- it is used to speed up searches using index
insert into users values(1,"anu","anu@gmail.com","anu@123","anu","radha","2002-12-17",now(),now(),'inactive');	
insert into users values(2,"getha","geethu@gmail.com","geeth@123","geetha","mari","2002-1-10",now(),now(),default);	
iNSERT INTO users (username, email, passwordHash, firstname, lastname, dateOfBirth, createdAt, lastLogin, status)
VALUES ('anju', 'anju@gmail.com', 'anju@123', 'anju', 'radha', '2006-1-15', NOW(), NOW(), 'suspended');
update users set lastlogin="2024-12-23 12:23:56" where userid=1;


select * from users;


create table Students(
stuid int primary key,
name varchar(255),
age int,
check(age>18));


create table enrollments(
enrollment_id int primary key,
student_id int,
course_id int,
foreign key(student_id) references Students(stuid));

insert into Students values(1,"rishmi",21),(2,"geetha",20);
insert into Students values(3,"abhi",17);
select * from Students;

insert into enrollments values(256,1,2002);
insert into enrollments values(700,2,2005);
select * from enrollments;


create table OrderDetails(
orderid int,
product_id int,
quantity int,
primary key(orderid,product_id));-- composite key  