create table Employees(empid int ,ename varchar(20),job_desc varchar(50));
use datarevature;
alter table Employees add column salary int;
alter table Employees add column hire_date int;

insert into Employees values(1,"ram","admin",25000,DATE '2015-11-23');
insert into Employees values(1,"radha","admin",25000,DATE '2015-11-23');
Insert into Employees values(2,"raghu","manager",450000,DATE '2013-09-23');
insert into Employees values(3,"geetha","sales",35000,DATE '2019-11-28');
insert into Employees values(4,"madhu","HR",250000,DATE '2012-11-23');
insert into Employees values(1,"radha","admin",85000,DATE '2015-11-23');
update Employees set salary=78000 where ename="ram";
update Employees set empid=2 where ename="ram";
select * from Employees;
select * from Employees order by job_desc;
-- drop table Employees;
-- average salary for eaxh dept
select job_desc,avg(salary) from employees group by job_desc;
-- count the number of employees of each dept
 select job_desc,count(empid) from Employees group by job_desc;
select job_desc from employees group by job_desc having count(empid)>1 order by job_desc;
SELECT job_desc, COUNT(empid) FROM employees
WHERE salary>50000 GROUP BY job_desc HAVING COUNT(empid)>1
ORDER BY job_desc;