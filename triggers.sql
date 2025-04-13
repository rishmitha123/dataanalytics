use dataanalytics;
CREATE TABLE items (

    id INT PRIMARY KEY, -- clustered index

    name VARCHAR(255) NOT NULL,

    price DECIMAL(10, 2) NOT NULL

);
 
INSERT INTO items(id, name, price) 

VALUES (1, 'Item', 50.00);
INSERT INTO items(id, name, price) VALUES (2, 'mobile', 50000),(3,"tv",25000);
 INSERT INTO items(id, name, price) VALUES(3,"tv",25000);
 
 
 CREATE TABLE item_changes (
    change_id INT PRIMARY KEY AUTO_INCREMENT,
    item_id INT,
    change_type VARCHAR(10),
    change_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (item_id) REFERENCES items(id)
);

DELIMITER //
CREATE TRIGGER Update_items
AFTER UPDATE
ON ITEMS
FOR EACH ROW
BEGIN
insert into item_changes(item_id,change_type) values(NEW.id,'update');
END;
//
SELECT * FROM items;
SELECT * FROM item_changes;
update items set name="laptop" where id=1;
-- trigger called after updation
SELECT * FROM items;
SELECT * FROM item_changes;
delete from items where id=2;
DELIMITER //
CREATE TRIGGER delete_items
BEFORE DELETE
ON ITEMS
FOR EACH ROW
BEGIN
insert into item_changes(item_id,change_type) values(OLD.id,'delete');
END;

ALTER TABLE item_changes 
ADD CONSTRAINT item 
FOREIGN KEY (item_id) REFERENCES items(id) 
ON DELETE SET NULL;
