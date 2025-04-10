use dataanalytics;
select * from employee;
-- fetch employees whose salary is less than average salary
select empname from employee where salary <
(select avg(salary) from employee);
-- fetch employees whose salary greater than average salary
select empname from employee where salary >
(select avg(salary) from employee);

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

INSERT INTO departments (department_id, department_name) VALUES

(1, 'Sales'),

(2, 'Marketing'),

(3, 'HR');
insert into departments values(4,'training');

INSERT INTO employees (employee_id, employee_name, department_id) VALUES
(101, 'Alice', 1),
(102, 'Bob', 1),
(103, 'Charlie', 2),
(104, 'Diana', 3);

select employee_name from employees where department_id =(select department_id from departments where department_name="Sales");

-- retrieve the employeee name along with their department name
select employee_name,(select department_name from departments where
departments.department_id=employees.department_id) as department_name from employees;

-- find employee who are in departmemnts who afre more than 1 
select employee_name from employees where department_id in(select department_id from employees group by department_id having count(*)>1);

-- find atleast one employee in departments
select department_id,department_name from departments d where exists
(select 1 from employees e where e.department_id=d.department_id);

-- find department who do not have employees
select department_id,department_name from departments d where  not exists
(select 1 from employees e where e.department_id=d.department_id);

-- find departmemnts where avg employee id has greater than 102
select department_id from employees group by department_id having avg(employee_id)>102;

select department_id from departments where department_id in
(select department_id from employees group by department_id having avg(employee_id)>102);

-- Scalar function operates on single value and returns a single value
