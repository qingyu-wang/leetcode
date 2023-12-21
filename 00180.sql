-- 180. Consecutive Numbers
-- https://leetcode.com/problems/consecutive-numbers/description/


-- Window Function: OVER, LEAD

SELECT 
    DISTINCT num1 AS ConsecutiveNums
FROM
    (
        SELECT 
            num AS num1,
            LEAD(num,1) OVER() AS num2,
            LEAD(num,2) OVER() AS num3
        FROM
            Logs
    ) AS t
WHERE
    num1 = num2
    AND num1 = num3;

-- 

SELECT 
    DISTINCT l1.num AS ConsecutiveNums
FROM
    Logs AS l1
    LEFT JOIN Logs AS l2 ON l1.id+1 = l2.id
    LEFT JOIN Logs AS l3 ON l1.id+2 = l3.id
WHERE
    l1.num = l2.num
    AND l1.num = l3.num;