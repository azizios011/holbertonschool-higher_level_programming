# SQL - Introduction

This project contains a series of SQL tasks that cover the fundamentals of working with databases using SQL (Structured Query Language). Each task focuses on different aspects of SQL, allowing you to gain a solid understanding of database management and data manipulation.

## Table of Contents

- [Task 0: List all Rows](#task-0-list-all-rows)
- [Task 1: Filter Records](#task-1-filter-records)
- [Task 2: Unique Records](#task-2-unique-records)
- [Task 3: Full Description](#task-3-full-description)
- [Task 4: Foreign Key Constraint](#task-4-foreign-key-constraint)
- [Task 5: Foreign Key Constraint #2](#task-5-foreign-key-constraint-2)
- [Task 6: List Values](#task-6-list-values)
- [Task 7: Insert Value](#task-7-insert-value)
- [Task 8: Count Records](#task-8-count-records)
- [Task 9: Full Creation](#task-9-full-creation)
- [Task 10: Top Score](#task-10-top-score)
- [Task 11: Best Score](#task-11-best-score)
- [Task 12: Update Record](#task-12-update-record)
- [Task 13: Remove Records](#task-13-remove-records)
- [Task 14: Score Average](#task-14-score-average)
- [Task 15: Group Records](#task-15-group-records)
- [Task 16: No Link](#task-16-no-link)

## Task 0: List all Rows

In this task, we learned how to list all rows from a given table in a database using a SQL script. The script used the `SELECT` statement to retrieve all records from the specified table.

## Task 1: Filter Records

In this task, we learned how to filter records based on certain conditions using the `WHERE` clause in a SQL script. The script used the `SELECT` statement along with the `WHERE` clause to retrieve specific records that met the specified conditions.

## Task 2: Unique Records

In this task, we learned how to list unique records from a table in a database using the `DISTINCT` keyword in a SQL script. The script used the `SELECT` statement along with the `DISTINCT` keyword to retrieve only distinct (unique) records from the specified table.

## Task 3: Full Description

In this task, we learned how to get the full description of a table in a database using the `DESCRIBE` statement or the `SHOW COLUMNS FROM` statement in a SQL script. The script used one of these statements to display the complete information about the columns in the specified table.

## Task 4: Foreign Key Constraint

In this task, we learned how to create a table with a foreign key constraint in a SQL script. The foreign key constraint ensures referential integrity between two tables, allowing us to link data from one table to another.

## Task 5: Foreign Key Constraint #2

In this task, we learned how to create a table with a foreign key constraint that references another table in a database using a SQL script. The foreign key constraint establishes a relationship between two tables based on a specified column.

## Task 6: List Values

In this task, we learned how to list all rows of a table in a database using a SQL script and how to pass the database name as an argument to the `mysql` command. The script used the `SELECT` statement to retrieve all records from the specified table and displayed all fields.

## Task 7: Insert Value

In this task, we learned how to insert a new row into a table in a database using a SQL script and how to pass the database name as an argument to the `mysql` command. The script used the `INSERT INTO` statement to add a new row with specified values into the specified table.

## Task 8: Count Records

In this task, we learned how to count the number of records that meet certain conditions in a table in a database using a SQL script and how to pass the database name as an argument to the `mysql` command. The script used the `SELECT COUNT(*)` statement along with the `WHERE` clause to count the number of rows that fulfilled specific conditions.

## Task 9: Full Creation

In this task, we learned how to create a new table in a database and insert multiple rows with specified data into the table using a SQL script and how to pass the database name as an argument to the `mysql` command. The script used the `CREATE TABLE IF NOT EXISTS` statement to create the table if it did not exist already and the `INSERT INTO` statement to add multiple rows with predefined values.

## Task 10: Top Score

In this task, we learned how to list all records of a table from a database using a SQL script, display specific columns, and order the records based on a particular column. The script used the `SELECT` statement to retrieve the `score` and `name` columns from the specified table and sorted the records by `score` in descending order.

## Task 11: Best Score

In this task, we learned how to list records that meet certain conditions from a table in a database using a SQL script and how to pass the database name as an argument to the `mysql` command. The script used the `SELECT` statement with the `WHERE` clause to filter records based on specific conditions and ordered the records by `score` in descending order.

## Task 12: Update Record

In this task, we learned how to update the values of specific columns in a table in a database using a SQL script and how to pass the database name as an argument to the `mysql` command. The script used the `UPDATE` statement with the `WHERE` clause to modify specific rows that met certain conditions.

## Task 13: Remove Records

In this task, we learned how to delete specific rows from a table in a database using a SQL script and how to pass the database name as an argument to the `mysql` command. The script used the `DELETE FROM` statement with the `WHERE` clause to remove rows that met certain conditions.

## Task 14: Score Average

In this task, we learned how to compute the average of values in a column of a table in a database using a SQL script and how to pass the database name as an argument to the `mysql` command. The script used the `SELECT` statement with the `AVG` function to calculate the average of values in the specified column.

## Task 15: Group Records

In this task, we learned how to group records based on specific columns in a table in a database using a SQL script and how to pass the database name as an argument to the `mysql` command. The script used the `SELECT` statement with the `GROUP BY` clause to group records

 based on the specified column and the `COUNT` function to count the number of records in each group.

## Task 16: No Link

In this task, we learned how to list records of a table from a database using a SQL script, display specific columns, and filter out rows that have a NULL value in a certain column. The script used the `SELECT` statement with the `WHERE` clause to exclude rows that had a NULL value in the `name` column and ordered the records by `score` in descending order.
--

These tasks provided a solid introduction to SQL and database management concepts, including querying, filtering, inserting, updating, and deleting data. With this knowledge, you are equipped to work with databases and manipulate data effectively using SQL.