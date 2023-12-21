-- 1731. The Number of Employees Which Report to Each Employee
-- https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/

SELECT
    m.employee_id,
    m.name,
    COUNT(e.employee_id) AS reports_count,
    ROUND(AVG(e.age)) AS average_age
FROM
    Employees AS e
    INNER JOIN Employees AS m ON e.reports_to = m.employee_id
GROUP BY
    m.employee_id
ORDER BY
    m.employee_id;

--

SELECT
    m.employee_id,
    m.name,
    COUNT(e.employee_id) AS reports_count,
    ROUND(AVG(e.age)) AS average_age
FROM
    Employees AS e
    LEFT JOIN Employees AS m ON e.reports_to = m.employee_id
WHERE
    e.reports_to IS NOT NULL
GROUP BY
    m.employee_id
ORDER BY
    m.employee_id;