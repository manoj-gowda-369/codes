CREATE TABLE students (
	id INT PRIMARY KEY,
	  name VARCHAR(50),
	marks INT
);
INSERT INTO students VALUES (1, 'Manoj', 85);
INSERT INTO students VALUES (2, 'Asha', 92);
INSERT INTO students VALUES (3, 'Raj', 74);

SELECT * FROM students WHERE marks > 80;
