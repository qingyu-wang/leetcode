-- 1907. Count Salary Categories
-- https://leetcode.com/problems/count-salary-categories/description/

SELECT 
    "Low Salary" AS category,
    SUM(income < 20000) AS accounts_count
FROM 
    Accounts

UNION

SELECT 
    "Average Salary" AS category,
    SUM(income BETWEEN 20000 AND 50000) AS accounts_count
FROM 
    Accounts

UNION

SELECT 
    "High Salary" AS category,
    SUM(income > 50000) AS accounts_count
FROM 
    Accounts;

-- 

SELECT
    t1.category,
    COUNT(t2.account_id) AS accounts_count
FROM 
    (
        SELECT 'Low Salary' AS category
        UNION 
        SELECT 'Average Salary' AS category
        UNION 
        SELECT 'High Salary' AS category
    ) AS t1
    LEFT JOIN (
        SELECT
            account_id,
            CASE 
                WHEN income < 20000 THEN 'Low Salary'
                WHEN income <= 50000 THEN 'Average Salary'
                WHEN income > 50000 THEN 'High Salary'
            END AS category
        FROM
            Accounts
    ) AS t2 ON t1.category = t2.category
GROUP BY
    t1.category;