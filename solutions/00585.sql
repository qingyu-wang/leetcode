-- 585. Investments in 2016
-- https://leetcode.com/problems/investments-in-2016/description/

SELECT
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM
    (
        SELECT
            *,
            COUNT(pid) OVER(PARTITION BY tiv_2015) AS tiv_2015_cnt,
            COUNT(pid) OVER(PARTITION BY lat, lon) AS lat_lon_cnt
        FROM
            Insurance
    ) AS t
WHERE
    tiv_2015_cnt != 1
    AND lat_lon_cnt = 1;

--

SELECT
    ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM
    Insurance
WHERE
    tiv_2015 IN (
        SELECT
            tiv_2015
        FROM
            insurance
        GROUP BY
            tiv_2015
        HAVING
            count(pid) > 1
    )
    AND (lat, lon) IN (
        SELECT
            lat,
            lon
        FROM insurance
        GROUP BY
            lat,
            lon
        HAVING
            count(pid) = 1
    );