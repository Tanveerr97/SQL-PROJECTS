-- Active: 1736099308663@@127.0.0.1@3306@project_1
CREATE TABLE Members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    phone_number VARCHAR(20),
    email VARCHAR(100),
    membership_date DATE NOT NULL
);
