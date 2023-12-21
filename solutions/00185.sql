-- 185. Department Top Three Salaries
-- https://leetcode.com/problems/department-top-three-salaries/description/

SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM
    (
        SELECT
            *,
            DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS r
        FROM
            Employee
    ) AS e
    LEFT JOIN Department AS d ON e.departmentId = d.id
WHERE
    e.r <= 3;