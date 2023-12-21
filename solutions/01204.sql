-- 1204. Last Person to Fit in the Bus
-- https://leetcode.com/problems/last-person-to-fit-in-the-bus/description/

WITH CTE AS (
    SELECT 
        *,
        SUM(weight) OVER(ORDER BY turn ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total_weight
    FROM 
        queue
)

SELECT 
    person_name 
FROM
    CTE 
WHERE 
    total_weight <= 1000 
ORDER BY 
    turn DESC
LIMIT
    1;

-- 

SELECT
    q1.person_name
FROM
    Queue AS q1
    CROSS JOIN Queue AS q2 ON q1.turn >= q2.turn
GROUP BY
    q1.turn
HAVING
    SUM(q2.weight) <= 1000
ORDER BY
    SUM(q2.weight) DESC
LIMIT
    1;

--

SELECT
    q1.person_name
FROM
    Queue AS q1
    CROSS JOIN Queue AS q2
GROUP BY
    q1.turn
HAVING
    SUM(CASE WHEN q1.turn >= q2.turn THEN q2.weight ELSE 0 END) <= 1000
ORDER BY
    SUM(CASE WHEN q1.turn >= q2.turn THEN q2.weight ELSE 0 END) DESC
LIMIT
    1;