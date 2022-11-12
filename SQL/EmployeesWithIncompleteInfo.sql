SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (SELECT DISTINCT(employee_id) FROM Salaries)
UNION
SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (SELECT DISTINCT(employee_id) FROM Employees)