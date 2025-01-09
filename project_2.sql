-- Active: 1736273532214@@127.0.0.1@3306@project_2
CREATE TABLE Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    dob DATE,
    email VARCHAR(100)
);
CREATE TABLE Subjects (
    subject_id INT PRIMARY KEY AUTO_INCREMENT,
    subject_name VARCHAR(100),
    teacher_name VARCHAR(100)
);
CREATE TABLE Marks (
    marks_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    subject_id INT,
    marks_obtained INT,
    exam_date DATE,
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
);
INSERT INTO Students (first_name, last_name, dob, email) VALUES
('John', 'Doe', '2000-05-15', 'john.doe@example.com'),
('Jane', 'Smith', '2001-07-22', 'jane.smith@example.com'),
('Alice', 'Johnson', '2002-02-28', 'alice.johnson@example.com'),
('Bob', 'Brown', '2000-11-10', 'bob.brown@example.com');
INSERT INTO Subjects (subject_name, teacher_name) VALUES
('Mathematics', 'Mr. Anderson'),
('Physics', 'Ms. Taylor'),
('Chemistry', 'Dr. White'),
('Biology', 'Dr. Green');
INSERT INTO Marks (student_id, subject_id, marks_obtained, exam_date) VALUES
(1, 1, 85, '2024-12-15'),
(1, 2, 78, '2024-12-15'),
(2, 1, 92, '2024-12-15'),
(2, 3, 88, '2024-12-15'),
(3, 2, 75, '2024-12-15'),
(3, 4, 95, '2024-12-15'),
(4, 1, 64, '2024-12-15'),
(4, 2, 70, '2024-12-15');
-- Get All Students with Their Marks
SELECT s.first_name, s.last_name, sub.subject_name, m.marks_obtained, m.exam_date
FROM Marks m
JOIN Students s ON m.student_id = s.student_id
JOIN Subjects sub ON m.subject_id = sub.subject_id
ORDER BY s.last_name, sub.subject_name;
-- Get Students Who Scored Above 80 in Mathematics
SELECT s.first_name, s.last_name, m.marks_obtained
FROM Marks m
JOIN Students s ON m.student_id = s.student_id
JOIN Subjects sub ON m.subject_id = sub.subject_id
WHERE sub.subject_name = 'Mathematics' AND m.marks_obtained > 80;
--  Get Average Marks for Each Student
SELECT s.first_name, s.last_name, AVG(m.marks_obtained) AS average_marks
FROM Marks m
JOIN Students s ON m.student_id = s.student_id
GROUP BY s.student_id
ORDER BY average_marks DESC;
--  Get Subject-wise Highest Marks
SELECT sub.subject_name, MAX(m.marks_obtained) AS highest_marks
FROM Marks m
JOIN Subjects sub ON m.subject_id = sub.subject_id
GROUP BY sub.subject_name
