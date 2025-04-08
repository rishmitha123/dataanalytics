use dataanalytics;
create table customers(customerid int primary key,name varchar(255));
create table orders(orderid int primary key,customer_id int,product varchar(255),foreign key(customer_id) references customers(customerid) ON DELETE CASCADE);
create table productdet(proid int primary key,customer_id int,pname varchar(25),FOREIGN KEY(customer_id) references customers(customerid)ON UPDATE CASCADE);
insert into productdet values(250,1,"pen"),(251,2,"pencil");
update customers set customerid=100 where customerid=1;
insert into customers values(1,"raghu"),(2,"geetha"),(3,"anju");
insert into orders values(101,1,"laptop"),(102,1,"mobile"),(103,2,"tv"),(104,3,"fridge");
select * from customers;
select * from orders;
select * from productdet;
drop table productdet;

-- on update cascade
CREATE TABLE Department (
  dept_id INT PRIMARY KEY,
  name VARCHAR(50)
);
CREATE TABLE Emp (
  emp_id INT PRIMARY KEY,
  name VARCHAR(50),
  dept_id INT,
  FOREIGN KEY (dept_id) REFERENCES Department(dept_id) ON UPDATE CASCADE
);

insert into department values(1,"IT"),(2,"nonIt"),(3,"service");
insert into Emp values(100,"anu",1),(101,"geetha",2);
select * from department;
select * from Emp;
delete from customers where customerid=3;
alter table productdet rename column pname to name;
create table employee(empid int primary key,empname varchar(255),salary int);
insert into employee values(1,"arjun",25000),(2,"giri",30000),(3,"rishmi",50000),(4,"vaishu",35000),(5,"shanu",45000);
select * from employee;
select * from employee order by salary;
alter table employee add column department varchar(255);
update employee set department="IT" where empid=1;
update employee set department="service" where empid=2;
update employee set department="non IT" where empid=3;
update employee set department="technical" where empid=4;
update employee set department="IT" where empid=5;
select * from employee order by department ASC ,salary DESC;
select * from employee order by department;
select * from employee order by salary DESC;
-- annual salary of a employee
select empid,empname,salary*12 as anualsalary,department from employee order by salary;