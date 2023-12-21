-- 1378. Replace Employee ID With The Unique Identifier
-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/

SELECT
    eu.unique_id AS unique_id,
    e.name AS name
FROM
    Employees AS e
    LEFT JOIN EmployeeUNI AS eu ON e.id = eu.id;