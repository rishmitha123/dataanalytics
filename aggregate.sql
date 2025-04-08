create table products(productid int,productname varchar(30),
price int);
use dataanalytics;
insert into products values(3,"breeza",300000),(2,"cycle",50000);
insert into products values(1,"bike",200000),(2,"car",250000);
update products set productid=4 where productname="cycle";
select * from products;
insert into products values(2,"scooter",650000);
insert into products values(1,"audi",950000),(3,"flight",780000);
-- aggregate functions 
select min(price) from products;
select max(price) as largeprice from products;
select min(price) as minimumPrice,productid from products group by productid;
select max(price) as maximumPrice,productid from products group by productid;
select sum(price) as sum,productid from products group by productid;
select avg(price) as avgerage,productid from products group by productid;
select count(*) as numberofColumns from products;
-- count of products where price>250000
select count(productid)from products where price>250000;
update products set price=650000 where productname="audi";
-- query to remove duplicate price value and return the count without duplicate
select count(distinct price) from products;