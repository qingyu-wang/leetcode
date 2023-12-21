-- 610. Triangle Judgement
-- https://leetcode.com/problems/triangle-judgement/description/

SELECT
    *,
    CASE WHEN 
        (x+y)>(z) 
        AND (x+z)>(y) 
        AND (y+z)>(x) 
        AND x>0 
        AND y>0 
        AND z>0 
        THEN 'Yes' ELSE 'No' 
    END AS triangle
FROM
    Triangle;