## Library Management System
    # well-structured for managing a library system. It includes tables for Books, Members, Transactions, Staff, Book Categories, and Categories. You've also included sample data insertions and a variety of useful queries for managing the library, such as borrowing books, checking overdue books, and retrieving available books.
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

CREATE TABLE Members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    phone_number VARCHAR(20),
    email VARCHAR(100),
    membership_date DATE NOT NULL
);
CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    member_id INT,
    check_out_date DATE NOT NULL,
    due_date DATE NOT NULL,
    check_in_date DATE,
    fine_amount DECIMAL(10, 2) DEFAULT 0.00,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);


INSERT INTO Books (title, author, genre, published_year, status)
VALUES 
    ('The Great Gatsby', 'F. Scott Fitzgerald', 'Fiction', 1925, 'Available'),
    ('1984', 'George Orwell', 'Dystopian', 1949, 'Available'),
    ('To Kill a Mockingbird', 'Harper Lee', 'Fiction', 1960, 'Checked-out'),
    ('The Catcher in the Rye', 'J.D. Salinger', 'Fiction', 1951, 'Available');
INSERT INTO Members (name, address, phone_number, email, membership_date)
VALUES
    ('John Doe', '123 Elm Street', '555-1234', 'john.doe@email.com', '2025-01-01'),
    ('Jane Smith', '456 Oak Avenue', '555-5678', 'jane.smith@email.com', '2025-01-02');
# book available or not
SELECT title, author, genre, published_year
FROM Books
WHERE status = 'Available';
#book out
INSERT INTO Transactions (book_id, member_id, check_out_date, due_date)
VALUES (1, 1, '2025-01-05', '2025-01-20');
UPDATE Books SET status = 'Checked-out' WHERE book_id = 1;
    #book in
UPDATE Transactions
SET check_in_date = '2025-01-22', fine_amount = DATEDIFF(CURRENT_DATE, due_date) * 2
WHERE transaction_id = 1;
    
UPDATE Books SET status = 'Available' WHERE book_id = 1;
    #over due book

SELECT b.title, m.name, t.due_date, DATEDIFF(CURRENT_DATE, t.due_date) AS overdue_days
FROM Transactions t
JOIN Books b ON t.book_id = b.book_id
JOIN Members m ON t.member_id = m.member_id
WHERE t.check_in_date IS NULL AND t.due_date < CURRENT_DATE;

;
    # overdue+fine
SELECT b.title, m.name, t.due_date, DATEDIFF(CURRENT_DATE, t.due_date) AS overdue_days, t.fine_amount
FROM Transactions t
JOIN Books b ON t.book_id = b.book_id
JOIN Members m ON t.member_id = m.member_id
WHERE t.check_in_date IS NULL AND t.due_date < CURRENT_DATE
ORDER BY overdue_days DESC;

-- SQLBook: Code

-- SQLBook: Markup
