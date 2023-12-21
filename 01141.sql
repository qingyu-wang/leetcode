-- 1141. User Activity for the Past 30 Days I
-- https://leetcode.com/problems/user-activity-for-the-past-30-days-i/description/

SELECT
    activity_date AS day,
    COUNT(DISTINCT user_id) AS active_users
FROM
    Activity
WHERE
    activity_date <= STR_TO_DATE('2019-07-27', '%Y-%m-%d')
    AND activity_date >= (STR_TO_DATE('2019-07-27', '%Y-%m-%d') - INTERVAL '29' DAY)
GROUP BY
    day;