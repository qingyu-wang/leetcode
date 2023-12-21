-- 1661. Average Time of Process per Machine
-- https://leetcode.com/problems/average-time-of-process-per-machine/description/

SELECT
    s.machine_id, 
    round(avg(e.timestamp-s.timestamp), 3) as processing_time
FROM
    Activity s
    INNER JOIN Activity e ON 
        s.machine_id = e.machine_id
        AND s.process_id = e.process_id
        AND s.activity_type = 'start'
        AND e.activity_type = 'end'
GROUP BY
    s.machine_id;

--

SELECT
    machine_id,
    ROUND(AVG(processing_time), 3) AS processing_time
FROM
    (
        SELECT
            machine_id,
            process_id,
            MAX(timestamp) - MIN(timestamp) AS processing_time
        FROM
            Activity
        GROUP BY
            machine_id,
            process_id
    ) AS t
GROUP BY
    machine_id;