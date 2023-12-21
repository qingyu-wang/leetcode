-- 550. Game Play Analysis IV
-- https://leetcode.com/problems/game-play-analysis-iv/description/

SELECT
    ROUND(COUNT(DISTINCT player_id)/(SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM
    Activity
WHERE
    (player_id, event_date - INTERVAL '1' DAY) IN (
        SELECT 
            player_id,
            MIN(event_date) AS event_date
        FROM
            Activity
        GROUP BY
            player_id
    );

-- 

SELECT
    ROUND(COUNT(DISTINCT a1.player_id)/(SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM
    (
        SELECT 
            player_id,
            MIN(event_date) AS event_date
        FROM
            Activity
        GROUP BY
            player_id
    ) AS a1
    INNER JOIN Activity AS a2 ON 
        a1.player_id = a2.player_id
        AND a1.event_date + INTERVAL '1' DAY = a2.event_date;