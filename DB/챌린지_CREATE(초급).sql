SELECT * FROM testdatabase.employees;
use testdatabase;
-- UPDATE employees
-- SET salary = salary * 1.1
-- WHERE position = 'PM';

-- UPDATE employees
-- SET salary = salary * 1.1
-- WHERE position = 'Backend';

-- DELETE FROM employees WHERE username = '민혁';

SELECT position, AVG(salary) AS average_salary FROM emplotees GROUP BY position;