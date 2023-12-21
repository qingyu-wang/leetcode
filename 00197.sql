-- 197. Rising Temperature
-- https://leetcode.com/problems/rising-temperature/description/

SELECT
    t.id AS id
FROM
    Weather AS t
    INNER JOIN Weather AS y ON t.recordDate - INTERVAL '1' DAY = y.recordDate
WHERE
    t.temperature > y.temperature;