use dataanalytics;

CREATE TABLE Customerstable (

    CustomerID INT PRIMARY KEY,

    CustomerName VARCHAR(100),

    ContactName VARCHAR(100),

    Country VARCHAR(50)

);
 
CREATE TABLE Orderstable (

    OrderID INT PRIMARY KEY,

    OrderDate DATE,

    CustomerID INT,

    Amount DECIMAL(10, 2),

    FOREIGN KEY (CustomerID) REFERENCES Customerstable(CustomerID)

);
 
INSERT INTO Customerstable (CustomerID, CustomerName, ContactName, Country) VALUES

(1, 'John Doe', 'John D.', 'USA'),

(2, 'Jane Smith', 'Jane S.', 'UK'),

(3, 'Alice Brown', 'Alice B.', 'Canada'),

(4, 'Bob Johnson', 'Bob J.', 'Australia');
 
INSERT INTO Orderstable (OrderID, OrderDate, CustomerID, Amount) VALUES

(101, '2024-09-01', 1, 250.00),

(102, '2024-09-05', 2, 300.00),

(103, '2024-09-07', 1, 150.00),

(104, '2024-09-10', 3, 450.00);

select * from Customerstable;
select * from  Orderstable;

select c.CustomerId,c.CustomerName,o.OrderId,o.OrderDate,o.Amount from Customerstable c inner join Orderstable o on c.CustomerId=o.CustomerId;
select c.CustomerId,c.CustomerName,o.OrderId,o.OrderDate,o.Amount from Customerstable c left join Orderstable o on c.CustomerId=o.CustomerId;
select c.CustomerId,c.CustomerName,o.OrderId,o.OrderDate,o.Amount from Customerstable c right join Orderstable o on c.CustomerId=o.CustomerId;
 select c.CustomerId,c.CustomerName,o.OrderId,o.OrderDate,o.Amount from Customerstable c  join Orderstable o on c.CustomerId=o.CustomerId;
 
 create table drink(id int primary key, drinks varchar(255));
 create table snacks(id int primary key,snack varchar(255));
 insert into drink values(1,"tea"),(2,"coffee"),(3,"shakes");
 insert into snacks values(1,"idly"),(2,"poori"),(3,"vada");
 select * from drink d cross join snacks s;
 
 
 