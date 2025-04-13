use dataanalytics;
-- views
select * from employees;

create view sales_employees as 
select employee_id,employee_name,department_id from employees
where department_id=2;

select * from departments;
select * from sales_employees;

-- giving the details of the employee along with their departmentmname
create view sales as 
select * ,(select department_name from departments where
departments.department_id=employees.department_id) as department_name from employees
where department_id =(select department_id from departments where department_name='sales') ;

select * from sales;
-- if table present it will modify or else it will create the new table
create or replace view sales_employees as 
select employee_id,employee_name,department_id from employees
where department_id=2;

drop view sales_employees;

-- the changes we made in the view it will effect the original table also
update sales_employees set employee_name='kohli' where employee_id=103;

select * from sales_employees;
select * from employees;
