-- E. SQLite Joins
-- 1. Write a query to find the addresses (location_id, street_address, city, state_province, country_name) of all the departments. 
-- SELECT department_name, department.location_id, street_address, city, state_province, country_name
-- FROM department
-- JOIN locations on department.location_id = locations.location_id
-- JOIN countries on locations.country_id = countries.country_id;
-- 2. Write a query to find the names (first_name, last name), department ID and the name of all the employees.
-- SELECT first_name || ' ' || last_name as name, department.department_id, department.department_name
-- FROM employees
-- LEFT JOIN department on department.department_id = employees.department_id;
-- 3. Write a query to find the employee id, name (last_name) along with their manager_id, manager name (last_name).
-- SELECT employee_id, last_name, manager_id, (SELECT last_name FROM employees emp2 WHERE emp1.manager_id = emp2.employee_id) as manager_name
-- FROM employees emp1;

-- 4. Write a query to find the names (first_name, last_name) and hire date of the employees who were hired after 'Jones'.
-- SELECT first_name || ' ' || last_name as name, hire_date
-- FROM employees
-- WHERE hire_date > (SELECT hire_date FROM employees WHERE last_name = 'Jones');

-- 5. Write a query to get the department name and number of employees in the department.
-- SELECT COUNT(employee_id) as 'number of employees in the department', department.department_name
-- FROM employees
-- JOIN department ON department.department_id = employees.department_id
-- GROUP BY employees.department_id;
-- 6. Write a query to find the employee ID, job title number of days between ending date and starting date for all jobs in department 90 from job history.
-- SELECT employee_id, job_id
-- FROM job_history
-- WHERE department_id = 90;
-- 7. Write a query to display the department ID, department name, and manager first name. 
-- SELECT department.department_id, department.department_name, employees.first_name
-- FROM department
-- JOIN employees ON employees.employee_id = department.manager_id;
-- 8. Write a query to display the department name, manager name, and city. 
-- SELECT department.department_id, department.department_name, employees.first_name||' '||employees.last_name AS name, locations.city
-- FROM department
-- JOIN employees ON employees.employee_id = department.manager_id
-- JOIN locations ON department.location_id = locations.location_id; 
-- 9. Write a query to display the job title and average salary of employees.
-- SELECT job_title, (SELECT SUM(salary)/COUNT(salary)  FROM employees)  as average_salary
-- FROM jobs;
-- 10. Write a query to to display job title, employee name, and the difference between the salary of the employee and minimum salary for the job.
-- SELECT jobs.job_title, employees.first_name||' '||employees.last_name AS name, MAX(employees.salary)-MIN(employees.salary) as 'difference salary'
-- FROM employees
-- JOIN jobs ON jobs.job_id = employees.job_id
-- GROUP BY employees.job_id;
-- 11. Write a query to display the job history that was done by any employee who is currently drawing more than 10000 of salary.
SELECT job_history.job_id
FROM job_history
JOIN employees ON employees.employee_id = job_history.employee_id
WHERE job_history.end_date < strftime('%Y-%m-%d','now') AND employees .salary > 10000;