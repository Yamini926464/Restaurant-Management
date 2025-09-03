create database Restaurant;
use Restaurant;

create table Menu (id int primary key, item_name varchar(100),item_price int ,item_price_in int,category varchar(100));
insert into Menu values(101,'Veg Manchow Soup',100,50,'Veg Soup'),(102,'Veg Hot And Sour Soup',100,50,'Veg Soup'),(103,'Tomato Soup',100,50,'Veg Soup'),(104,'Chicken Manchow Soup',130,70,'Non-Veg Soup'),(105,'Chicken Hot And Sour Soup',130,70,'Non-Veg Soup');
insert into Menu values(106,'Chilli Baby Corn',209,120,'Veg Starter'),(107,'Paneer 65',209,150,'Veg Starter'),(108,'Chilli Paneer',249,150,'Veg Starter'),(109,'Mushroom 65',209,130,'Veg Starter'),(110,'Chilli Mushroom',219,130,'Veg Starter');
insert into Menu values(111,'Chicken 65',239,170,'Non-Veg Starter'),(112,'Chilli Chicken',239,170,'Non-Veg Starter'),(113,'Chicken Lollipop',259,170,'Non-Veg Starter'),(114,'Chicken Wings',259,170,'Non-Veg Starter'),(115,'Chicken Joints',249,170,'Non-Veg Starter'),(116,'Chicken Majestic',259,170,'Non-Veg Starter'),(117,'Chicken Manchuri',239,170,'Non-Veg Starter'),(118,'Koujapitta-2Pcs',170,100,'Non-Veg Starter'),(119,'Apollo Fish',299,200,'Non-Veg Starter'),(120,'Chilli Prawns',299,210,'Non-Veg Starter'),(121,'Prawns 65',299,210,'Non-Veg Starter'),(122,'Prawns Manchuria',299,210,'Non-Veg Starter');
insert into Menu values(123,'Pulka',10,8,'Bread'),(124,'Butter Pulka',20,15,'Bread'),(125,'Roti',25,15,'Bread'),(126,'Butter Roti',30,20,'Bread'),(127,'Plain Naan',35,20,'Bread'),(128,'Butter Naan',40,25,'Bread'),(129,'Romali Roti',50,30,'Bread'),(130,'Aloo Parathai',50,30,'Bread');
insert into Menu values(131,'Palak Paneer',170,100,'Veg Curry'),(132,'Paneer Butter Masala',220,110,'Veg Curry'),(133,'Kaaju Paneer',240,150,'Veg Curry'),(134,'Kadai Paneer',220,100,'Veg Curry'),(135,'Mixed Veg Curry',179,100,'Veg Curry'),(136,'Kaaju Tomato Curry',220,150,'Veg Curry'),(137,'Mushroom Masala',239,100,'Veg Curry'),(138,'Kaaju Mushroom Masala',249,170,'Veg Curry'),(139,'Paneer Tikka Masala',259,120,'Veg Curry');
insert into Menu values(140,'Anda Masala',159,80,'Non-Veg Curry'),(141,'Anda Burji',169,100,'Non-Veg Curry'),(142,'Tomato Anda Curry',189,100,'Non-Veg Curry'),(143,'Chicken Curry',200,120,'Non-Veg Curry'),(144,'Boneless Chicken Curry',240,140,'Non-Veg Curry'),(145,'Boneless Chicken Fry',240,150,'Non-Veg Curry'),(146,'Chicken Fry',200,140,'Non-Veg Curry'),(147,'Butter Chicken',240,140,'Non-Veg Curry'),(148,'Kadai Chicken Curry',240,140,'Non-Veg Curry'),(149,'Cashew Chicken Curry',240,160,'Non-Veg Curry'),(150,'Moghalai Chicken Curry',260,140,'Non-Veg Curry');
insert into Menu values(151,'Veg Dum Biryani',230,150,'Veg Biriyani'),(152,'Kaaju Panner Biryani',300,200,'Veg Biriyani'),(153,'Shahi Paneer Biryani',320,210,'Veg Biriyani'),(154,'Shahi Mushroom Biryani',270,150,'Veg Biriyani'),(155,'Kaaju Mushroom Biryani',300,180,'Veg Biriyani');
insert into Menu values(156,'Egg Biryani',200,120,'Non-Veg Biriyani'),(157,'Chicken  Dum Biryani',280,180,'Non-Veg Biriyani'),(158,'Chicken Fry Biryani',290,180,'Non-Veg Biriyani'),(159,'Boneless Chicken Biryani',320,200,'Non-Veg Biriyani'),(160,'Chicken Lollipop Biryani',320,200,'Non-Veg Biriyani'),(161,'Chicken Wings Biryani',320,200,'Non-Veg Biriyani'),(162,'Kaaju Chicken Biryani',340,220,'Non-Veg Biriyani'),(163,'Mughalai Chicken Biryani',340,200,'Non-Veg Biriyani'),(164,'Mutton Fry Biryani',360,220,'Non-Veg Biriyani'),(165,'Naatukodi Biryani',340,250,'Non-Veg Biriyani'),(166,'Prawns Fry Biryani',350,250,'Non-Veg Biriyani'),(167,'Fish Biryani',350,220,'Non-Veg Biriyani'),(168,'Kamjupitta Biryani',350,360,'Non-Veg Biriyani');
insert into Menu Values(169,'Water Bottle(1 Liter)',25,20,'Beverage'),(170,'Water Bottle(Half Liter)',15,10,'Beverage'),(171,'90s Swag Soda',25,20,'Beverage'),(172,'Cool Drinks(250 ml)',25,20,'Beverage');

select* from Menu;   
create table orders(order_id int primary key, item_name varchar(100),
 quantity int, total_price int,order_datetime datetime, mobile varchar(15));

select*from Orders;       
desc orders;
desc menu;



