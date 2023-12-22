-- 1321. Restaurant Growth
-- https://leetcode.com/problems/restaurant-growth/description/

SELECT 
    d.visited_on AS visited_on, 
    SUM(c.amount) AS amount, 
    ROUND(SUM(c.amount) / 7, 2) AS average_amount
FROM 
    (
        SELECT 
            DISTINCT visited_on 
        FROM 
            Customer
        WHERE 
            (visited_on - INTERVAL 6 DAY) >= (SELECT MIN(visited_on) FROM Customer)
    ) AS d
    LEFT JOIN Customer c ON DATEDIFF(d.visited_on, c.visited_on) BETWEEN 0 and 6
GROUP BY
    d.visited_on;

-- 

SELECT
    visited_on,
    amount,
    ROUND(amount/7, 2) AS average_amount
FROM
    (
        SELECT
            visited_on,
            SUM(amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount
        FROM 
            (
                SELECT
                    visited_on,
                    SUM(amount) AS amount,
                    COUNT(amount) AS cnt
                FROM
                    Customer
                GROUP BY
                    visited_on
            ) AS t
    ) AS t
WHERE
    (visited_on - INTERVAL 6 DAY) IN (
        SELECT
            visited_on
        FROM
            Customer
    );