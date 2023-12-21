-- 1729. Find Followers Count
-- https://leetcode.com/problems/find-followers-count/description/

SELECT
    user_id,
    COUNT(DISTINCT follower_id) AS followers_count
FROM
    Followers
GROUP BY
    user_id;