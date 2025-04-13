use dataanalytics;
select * from customers;
start transaction;
savepoint point;
insert into customers values(5,"juunu");
commit;
savepoint hello;
insert into customers values(6,"arjunyy");
rollback to point;
-- PROCEDURES
DELIMITER //
CREATE PROCEDURE GETALLUSERS()
BEGIN
SELECT * FROM USER;
END;
//
CALL GETALLUSERS()

DELIMITER //
CREATE PROCEDURE DET(IN USER_ID INT)
BEGIN
SELECT USER_ID,NAME FROM USER where userid=USER_ID;
END
//

CALL DET(102);
DELIMITER //
CREATE PROCEDURE GETUSERNAME(IN USER_ID INT,OUT Username VARCHAR(50))
BEGIN
SELECT name INTO Username FROM USER WHERE USER_ID=userid;
END;
//

SET @Username='';
CALL GETUSERNAME(102,@Username);
select @Username;


