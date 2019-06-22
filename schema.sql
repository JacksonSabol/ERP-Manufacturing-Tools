DROP DATABASE IF EXISTS erp_manufacturing_tools;

CREATE DATABASE erp_manufacturing_tools;

USE erp_manufacturing_tools;

CREATE TABLE sales
(
	id int NOT NULL AUTO_INCREMENT,
	department_name varchar(255) NOT NULL,
    amount DECIMAL(13,2) NOT NULL,
    created_at TIMESTAMP default CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);