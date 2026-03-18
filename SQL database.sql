create database data_sales;

use data_sales;

create table tb_products(
id int(3) auto_increment primary key,
name_product varchar(100) not null,
price float(6.2) not null,
description_product varchar(500),
category varchar(100),
image varchar(300),
rate float(4.2),
count int(5)
);

SELECT * from tb_products;

-- Test query for verifying if there are more than one product
select name_product, count(name_product) as qtd_names 
from tb_products
group by name_product;


