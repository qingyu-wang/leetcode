-- 1934. Confirmation Rate
-- https://leetcode.com/problems/confirmation-rate/description/

SELECT
    s.user_id,
    ROUND(AVG(IF(c.action='confirmed', 1, 0)), 2) AS confirmation_rate
FROM
    Signups AS s
    LEFT JOIN Confirmations AS c ON s.user_id = c.user_id
GROUP BY
    s.user_id

-- 

SELECT
    s.user_id,
    ROUND(IF(COUNT(c.action)!=0, SUM(IF(c.action='confirmed', 1, 0)) / COUNT(c.action), 0), 2) AS confirmation_rate
FROM
    Signups AS s
    LEFT JOIN Confirmations AS c ON s.user_id = c.user_id
GROUP BY
    s.user_id