-- 196. Delete Duplicate Emails
-- https://leetcode.com/problems/delete-duplicate-emails/description/

DELETE 
    p1 
FROM 
    Person p1
    CROSS JOIN Person p2 
WHERE 
    p1.email = p2.email 
    AND p1.id > p2.id;

-- 

DELETE 
FROM 
    Person 
WHERE 
    id NOT IN (
        SELECT 
            *
        FROM
            (
                SELECT
                    MIN(id)
                FROM
                    Person
                GROUP BY
                    email
            ) AS t
    );