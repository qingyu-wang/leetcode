-- 1633. Percentage of Users Attended a Contest
-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/description/


SELECT
    contest_id,
    ROUND(COUNT(user_id)/(SELECT COUNT(DISTINCT user_ID) FROM Users)*100, 2) AS percentage
FROM
    Register
GROUP BY
    contest_id
ORDER BY
    percentage DESC,
    contest_id;

-- 

SELECT
    t1.contest_id,
    ROUND(AVG(IF(t2.user_id IS NULL, 0, 100)), 2) AS percentage
FROM
    (
        SELECT
            r.contest_id,
            u.user_id
        FROM
            Register AS r 
            CROSS JOIN Users AS u
        GROUP BY
            r.contest_id,
            u.user_id
    ) AS t1
    LEFT JOIN Register AS t2 ON 
        t1.contest_id = t2.contest_id
        AND t1.user_id = t2.user_id
GROUP BY
    t1.contest_id
ORDER BY
    percentage DESC,
    t1.contest_id;