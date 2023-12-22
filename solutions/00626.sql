-- 626. Exchange Seats
-- https://leetcode.com/problems/exchange-seats/description/

SELECT
    id,
    IF(
        MOD(id, 2)=1 ,
        LEAD(student, 1, student) OVER(),
        LAG(student, 1, student) OVER()
    ) AS student
FROM
    Seat;

--

SELECT
    s.id,
    CASE
        WHEN s.id = (SELECT COUNT(*) FROM Seat) AND s.id % 2 = 1 THEN s.student
        WHEN s.id % 2 = 1 THEN s2.student
        WHEN s.id % 2 = 0 THEN s1.student
        ELSE "Unknown"
    END AS student
FROM
    Seat AS s
    LEFT JOIN (
        SELECT
            id+1 AS id,
            student
        FROM
            Seat
    ) AS s1 ON s.id = s1.id
    LEFT JOIN (
        SELECT
            id-1 AS id,
            student
        FROM
            Seat
    ) AS s2 ON s.id = s2.id;