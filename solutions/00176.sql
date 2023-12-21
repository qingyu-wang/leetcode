-- 176. Second Highest Salary
-- https://leetcode.com/problems/second-highest-salary/description/

SELECT
    (
        SELECT 
            DISTINCT salary
        FROM 
            Employee 
        ORDER BY 
            salary DESC 
        LIMIT
            1
        OFFSET
            1
    ) AS SecondHighestSalary;

--

SELECT
    LEAD(salary, 1) OVER() as SecondHighestSalary
FROM
    (
        SELECT
            DISTINCT salary
        FROM Employee
    ) AS t
ORDER BY
    salary DESC
LIMIT
    1;