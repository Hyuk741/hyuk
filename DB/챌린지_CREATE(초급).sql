SELECT * FROM testdatabase.employees;
-- employees 테이블 생성
--  CREATE TABLE employees(
--        user_id INT AUTO_INCREMENT PRIMARY KEY,
--        username VARCHAR(100),
--        position VARCHAR(100),
--        salary DECIMAL(10, 2)
-- );

-- 직원 데이터 추가
-- INSERT INTO employees (username, position, salary)
-- VALUES('혜린', 'PM', 90000),
-- 	  ('은우', 'Frontend', 80000),
--       ('가을', 'Backend', 92000),
--       ('지수', 'Frontend', 78000),
--       ('민혁', 'Frontend', 96000),
--       ('하온', 'Backend', 130000);

-- 직원 이름 연봉 정보 조회 쿼리문
-- SELECT* FROM employees;

-- frontend 직책 연봉 90000이하 이름 연봉 조회
-- SELECT username, salary FROM employees WHERE position = 'Frontend' AND salary <= 90000;

-- PM직책 연봉 10% 인상
-- UPDATE employees SET salary = salary * 1.1 WHERE position = 'PM';

-- 모든 Backend 연봉 5%인상
-- UPDATE employees SET salary = salary * 1.05
-- WHERE position = 'Backend';

-- 민혁 사원 데이터 삭제
-- DELETE FROM employees
-- WHERE name = '민혁';

-- 모든직원 그룹화
-- SELECT position, AVG(salary)
-- AS average_salary
-- FROM employees GROUP BY position;

-- 데이터 삭제
-- DROP TABLE employees;