create database	workerdb;
use workerdb;


drop table worker;

create table worker(
	worker_id int auto_increment not null primary key,
    first_name varchar(50),
    last_name varchar(50),
    salary int,
    joining_date  varchar(100),
    Department varchar(20));
    

select * from worker;
INSERT INTO worker (first_name, last_name, salary, joining_date, Department)
VALUES ('Monika', 'Arora', 100000, '2/12/2014 9:0', 'HR');
INSERT INTO worker (first_name, last_name, salary, joining_date, Department)
values ('Niharika','Varma',80000,'6/11/2014 9:0','Admin');
INSERT INTO worker (first_name, last_name, salary, joining_date, Department)
values ('vishal','singhal',300000, '2/20/2014 9:0','HR');
INSERT INTO worker (first_name, last_name, salary, joining_date, Department)
values ('Amitabh','singh',500000,'2/20/2014 9:0','Admin');
INSERT INTO worker (first_name, last_name, salary, joining_date, Department)
values ('vivek','Bhati',500000, '6/11/2014 9:0','Admin');
INSERT INTO worker (first_name, last_name, salary, joining_date, Department)
values ('Vipul','Diwan',200000, '6/11/2014 9:0', 'Account');
INSERT INTO worker (first_name, last_name, salary, joining_date, Department)
values ('Satish','kumar',75000, '1/20/2014 9:0', 'Account');
INSERT INTO worker (first_name, last_name, salary, joining_date, Department)
values ('Geetika','Chauhan',90000, '4/11/2014 9:0','Admin');
select * from worker;

-- 1. Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME 
 -- Ascending and DEPARTMENT Descending.
 
 select *from worker 
 order by first_name , Department desc ;
 
 -- 2.Write an SQL query to print details for Workers with the first names “Vipul” and “Satish” 
-- from the Worker table

select * from worker
where Department like "Account";

-- 3. Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and 
-- contains six alphabets.

select * from worker
where first_name like "%h" and char_length(first_name) = 6;

-- 4. Write an SQL query to print details of the Workers whose SALARY lies between 1. 

select * from worker
where salary between 0 and 100000;

-- 5. Write an SQL query to fetch duplicate records having matching data in some fields of a table. 
/*SELECT column1, column2, COUNT(*)
FROM table_name
GROUP BY column1, column2
HAVING COUNT(*) > 1;
*/
select first_name,last_name ,count(*) from worker
group by first_name,last_name
having count(*)>1;

-- 6. Write an SQL query to show the top 6 records of a table. 
select * from worker
where worker_id<=6;

-- 7. Write an SQL query to fetch the departments that have less than five people in them. 
SELECT Department
FROM worker
GROUP BY Department
HAVING COUNT(*) < 5;

-- 8. Write an SQL query to show all departments along with the number of people in there. 

SELECT Department, COUNT(*) as Num_of_people
FROM worker
GROUP BY Department;

-- 9. Write an SQL query to print the name of employees having the highest salary in each 
-- department.

SELECT Department, first_name, last_name, salary 
FROM worker
WHERE (Department, salary) IN 
    (SELECT Department, MAX(salary)
     FROM worker
     GROUP BY Department);


-- Qus-2

create  database open_school_db;
use open_school_db;
drop table student;

create table student (
	stdID  int  not null primary key ,
    stdName varchar(100),
    Sex varchar(6),
    percentage int,
    class int,
    Sec varchar(2),
    Stream varchar(10),
    DOB varchar(50));

select * from student;
insert into student(stdID,stdName,sex,percentage,class,Sec,Stream,DOB)
values
(1001,'Surekha Joshi','Female',82,12,'A','Science', '3/8/1998'),
(1002,'MAAHI AGARWAL','Female',56,11,'C','Commerce','11/23/2008'),
(1003,'Sanam Verma','male',59,11,'C','Commerce', '6/29/2006'),
(1004,'Ronit Kumar','male',63,11,'C','commerce', '11/5/1997'),
(1005,'Dipesh Pulkit','male',78,11,'B','Science', '1/09/2003'),
(1006,'JAHANVI Puri','Female',60,11,'B','commerce', '11/7/2008'),
(1007,'Sanam kumar','male',23,12,'F','commerce', '3/8/1998'),
(1008,'SAHIL SARAS','male',56,11,'C','commerce', '11/7/2008'),
(1009,'AKSHRA AGARWAL','Female',72,12,'B','commerce', '10/1/1996'),
(1010,'STUTI MISHRA','Female',39,11,'F','Science', '11/23/2008'),
(1011,'HARSH AGARWAL','male',42,11,'C','Science', '3/8/1998'),
(1012,'NIKUNJ AGARWAL','male',49,12,'C','commerce', '8/06/1998'),
(1013,'AKRITI SAXENA','Female',89,12,'A','Science', '11/23/2008'),
(1014,'TANI RASTOGI','Female',82,12,'A','Science', '11/23/2008');


-- 1 To display all the records form STUDENT table. 
SELECT * FROM student ; 

-- 2 . To display any name and date of birth from the table STUDENT. 
SELECT StdName, DOB 
FROM student ;

-- 3 . To display all students record where percentage is greater of equal to 80 FROM student table. 
SELECT * FROM student WHERE percentage >= 80;

-- 4. To display student name, stream and percentage where percentage of student is more than 80 
SELECT stdName, Stream, Percentage  from student
WHERE percentage > 80;

-- 5. To display all records of science students whose percentage is more than 75 form student table. 
SELECT * From student 
WHERE Stream like 'Science' AND percentage > 75; 
