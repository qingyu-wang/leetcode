-- 570. Managers with at Least 5 Direct Reports
-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/

SELECT
    m.name
FROM
    Employee AS e
    INNER JOIN Employee AS m ON e.managerID = m.id
WHERE
    e.managerID IS NOT NULL
GROUP BY
    e.managerID
HAVING
    COUNT(e.ID) >= 5;

-- 

SELECT
    name
FROM
    (
        SELECT
            m.name,
            COUNT(e.ID) AS direct_report
        FROM
            Employee AS e
            INNER JOIN Employee AS m ON e.managerID = m.id
        WHERE
            e.managerID IS NOT NULL
        GROUP BY
            e.managerID
    ) AS t
WHERE
    direct_report >= 5;