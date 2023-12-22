-- 602. Friend Requests II: Who Has the Most Friends
-- https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/

SELECT 
    id, 
    COUNT(id) AS num
FROM
    (
        SELECT 
            requester_id AS id
        FROM 
            RequestAccepted
        UNION ALL
        SELECT 
            accepter_id AS id
        FROM 
            RequestAccepted
    ) AS t
GROUP BY 
    id
ORDER BY 
    num DESC
LIMIT 
    1;

-- 

SELECT
    f.id,
    COALESCE(fr.friend_r, 0) + COALESCE(fa.friend_a, 0) AS num
FROM
    (
        SELECT
            requester_id AS id
        FROM
            RequestAccepted
        UNION
        SELECT
            accepter_id AS id
        FROM
            RequestAccepted
    ) AS f
    LEFT JOIN (
        SELECT
            accepter_id AS id,
            COUNT(requester_id) AS friend_r
        FROM
            RequestAccepted
        GROUP BY
            accepter_id
    ) AS fr ON f.id = fr.id
    LEFT JOIN (
        SELECT
            requester_id AS id,
            COUNT(accepter_id) AS friend_a
        FROM
            RequestAccepted
        GROUP BY
            requester_id
    ) AS fa ON f.id = fa.id
ORDER BY
    num DESC
LIMIT
    1;