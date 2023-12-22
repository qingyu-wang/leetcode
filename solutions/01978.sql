-- 1978. Employees Whose Manager Left the Company
-- https://leetcode.com/problems/employees-whose-manager-left-the-company/description/

SELECT
    e.employee_id
FROM 
    Employees AS e
    LEFT JOIN Employees AS m ON e.manager_id = m.employee_id
WHERE
    e.salary < 30000
    AND e.manager_id IS NOT NULL
    AND m.name IS NULL
ORDER BY
    employee_id;