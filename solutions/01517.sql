-- 1517. Find Users With Valid E-Mails
-- https://leetcode.com/problems/find-users-with-valid-e-mails/description/

SELECT
    *
FROM
    Users
WHERE
    LOWER(mail) REGEXP '^[a-z][a-z0-9_.-]*@leetcode[.]com$';

--

SELECT
    *
FROM
    Users
WHERE
    REGEXP_LIKE(mail, '^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$');

--

SELECT
    *
FROM
    Users
WHERE
    REGEXP_LIKE(mail, '^[a-zA-Z][a-zA-Z0-9\\_\\.\\-]*\\@leetcode\\.com$');