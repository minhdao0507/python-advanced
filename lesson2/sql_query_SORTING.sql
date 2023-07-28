-- B. SQLite Restricting and Sorting Data 

-- 1. Write a query to display the names (first_name, last_name) and salary for all employees whose salary is not in the range $10,000 through $15,000.
--SELECT first_name || ' ' || last_name as name, salary FROM employees WHERE salary NOT BETWEEN 10000 AND 15000 ;
-- 2. Write a query to display the names (first_name, last_name) and department ID of all employees in departments 30 or 100 in ascending alphabetical order by department ID. 
--SELECT first_name || ' ' || last_name as name,  department_id FROM employees WHERE department_id = 30 OR department_id =100 ORDER BY department_id, name ASC;
-- 3. Write a query to display the names (first_name, last_name) and salary for all employees whose salary is not in the range $10,000 through $15,000 and are in department 30 or 100.
--SELECT first_name || ' ' || last_name as name, salary, department_id FROM employees WHERE salary NOT BETWEEN 10000 AND 15000 AND department_id = 30 OR department_id =100;
-- 4. Write a query to display the first_name of all employees who have both an "b" and "c" in their first name.
--SELECT first_name FROM employees WHERE instr(first_name, 'b') AND instr(first_name, 'c');
-- 5. Write a query to display the last name, job, and salary for all employees whose job is that of a Programmer or a Shipping Clerk, and whose salary is not equal to $4,500, $10,000, or $15,000.
--SELECT first_name || ' ' || last_name as name, job_id, salary FROM employees WHERE job_id = 'IT_PROG';
-- 6. Write a query to display the last names of employees whose names have exactly 6 characters. 
--SELECT last_name FROM employees WHERE length(last_name) = 6;

-- 7. Write a query to display the last names of employees having 'e' as the third character.
--SELECT last_name FROM employees WHERE instr(last_name,'c' ) = 3;
-- 8. Write a query to display the jobs/designations available in the employees table. 
--SELECT DISTINCT job_id FROM employees;
-- 9. Write a query to display the names (first_name, last_name), salary and PF (15% of salary) of all employees. 
SELECT first_name || ' ' || last_name as name, salary, salary*0.15 as PF FROM employees;