-- 1683. Invalid Tweets
-- https://leetcode.com/problems/invalid-tweets/description/

SELECT
    tweet_id
FROM
    Tweets
WHERE
    CHAR_LENGTH(content) > 15;