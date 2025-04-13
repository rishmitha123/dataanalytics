use dataanalytics;
-- window functions
CREATE TABLE employ (

    employee_id INT PRIMARY KEY,

    name VARCHAR(50),

    department VARCHAR(50),

    salary INT

);
 
INSERT INTO employ (employee_id, name, department, salary) VALUES

(1, 'Alice',   'Sales', 50000),

(2, 'Bob',     'Sales', 60000),

(3, 'Charlie', 'Sales', 45000),

(4, 'David',   'IT',    70000),
(5, 'Eva',     'IT',    80000),

(6, 'Frank',   'IT',    75000);
insert into employ values(7, 'samuel',   'IT',    70000);

select employee_id,name,department,salary,ROW_NUMBER()
OVER (PARTITION BY department order by salary desc)
as rank_in_dept from employ; 

select employee_id,name,salary,sum(salary) over(order by salary) as running_total from employ;

select employee_id,name,salary,
lag(salary) over(order by salary) as prev_salary,
lead(salary) over(order by salary) as next_salary
from employ;

select employee_id,name,department,salary,RANK()
OVER (PARTITION BY department order by salary desc)
as salary_rank from employ; 

select employee_id,name,department,salary,DENSE_RANK()
OVER (PARTITION BY department order by salary desc)
as salary_rank from employ; 

SELECT employee_id,name,salary,NTILE(4) over(order by salary desc)
as quarter from employ;
use dataanalytics;

-- userdefined functions
DELIMITER //
CREATE FUNCTION CalculateRectangleArea(length float,width float)
returns float
DETERMINISTIC -- returns the same result if we give same input an it is mandatory
BEGIN
RETURN length*width;
END;
//
SELECT CalculateRectangleArea(5.5,2.3) AS AREA;

DELIMITER //
CREATE FUNCTION CalculateSquareArea(side int)
returns int
 -- returns the same result if we give same input
BEGIN
RETURN side*side;
END;
//
SELECT CalculateSquareArea(5) AS AREA;

select empid,empname,salary,
case
when salary>50000 then "high"
when salary between 10000 and 50000 then "medium"
else 'low'
end as salary_guide from employee;

select * from employee;
select empid,empname,salary  
salary=case
		when salary=50000 THEN 'Priority'
		else 'standard'
		end as priorities from employee;

select name,age,
case
when age<18 then 'minor'
when age between 18 and 59 then 'adult'
else 'senior'
end as age_group from people;

select empname,salary,
case
when salary<10000 then 'minor'
when salary between 20000 and 40000 then 'adult'
else 'senior'
end as age_group from employee

update students 
set grade=
case
when marks>=90 then 'A'
when marks>=75 then 'B'
when marks>=60 then 'C'
ELSE 'D'
END;

explain select * from employees where department_id=2;

update EMPLOYEE
set salary=
case
when salary>=49000 then 'A'
when salary>=35000 then 'B'
when salary>=20000 then 'C'
ELSE 'D'
END;

create table userdet(
id int,
profile JSON);
insert into userdet values(1,'{"name":"alice","skills":["sql","python"]}');
select JSON_EXTRACT(profile,'$.skills[1]') from userdet;