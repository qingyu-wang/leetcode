-- 619. Biggest Single Number
-- https://leetcode.com/problems/biggest-single-number/description/

SELECT
    MAX(num) AS num
FROM
    (
        SELECT
            num
        FROM
            MyNumbers
        GROUP BY
            num
        HAVING
            COUNT(num) = 1
    ) AS t;