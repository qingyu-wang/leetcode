-- 1667. Fix Names in a Table
-- https://leetcode.com/problems/fix-names-in-a-table/description/

SELECT
    user_id,
    CONCAT(UPPER(SUBSTRING(name, 1, 1)), LOWER(SUBSTRING(name, 2))) AS name
FROM 
    Users
ORDER BY
    user_id;