-- 1789. Primary Department for Each Employee
-- https://leetcode.com/problems/primary-department-for-each-employee/description/

SELECT 
    employee_id, 
    department_id 
FROM 
    (
        SELECT 
            *, 
            COUNT(employee_id) OVER(PARTITION BY employee_id) AS EmployeeCount
        FROM 
            Employee
    ) AS EmployeePartition 
WHERE 
  EmployeeCount = 1 
  OR primary_flag = 'Y';

-- 

SELECT
    employee_id,
    department_id
FROM
    Employee
GROUP BY
    employee_id
HAVING
    COUNT(employee_id) = 1

UNION

SELECT
    employee_id,
    department_id
FROM
    Employee
WHERE
    primary_flag = 'Y';

--

SELECT
    employee_id,
    department_id
FROM
    Employee
WHERE
    (employee_id, department_id) IN (
        SELECT
            employee_id,
            department_id
        FROM
            Employee
        GROUP BY
            employee_id
        HAVING
            COUNT(department_id) = 1
    )
    OR (employee_id, department_id) IN (
        SELECT
            employee_id,
            department_id
        FROM
            Employee
        WHERE
            primary_flag = 'Y'
    );