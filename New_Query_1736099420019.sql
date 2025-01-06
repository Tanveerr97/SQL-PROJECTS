-- SQLBook: Code
-- Active: 1736099308663@@127.0.0.1@3306@project_1
CREATE TABLE Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    genre VARCHAR(100),
    published_year YEAR,
    status VARCHAR(20) CHECK(status IN ('Available', 'Checked-out')) DEFAULT 'Available'
);
