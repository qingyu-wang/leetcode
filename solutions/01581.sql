-- 1581. Customer Who Visited but Did Not Make Any Transactions
-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/

SELECT
    v.customer_id,
    COUNT(v.visit_id) AS count_no_trans
FROM
    Visits AS v
    LEFT JOIN Transactions AS t ON v.visit_id = t.visit_id
WHERE
    t.transaction_id IS NULL
GROUP BY
    v.customer_id;

--

SELECT
    v.customer_id,
    COUNT(v.visit_id) AS count_no_trans
FROM
    Visits AS v
    LEFT JOIN (
        SELECT 
            visit_id, 
            COALESCE(amount, -1) as amount 
        FROM 
            Transactions
    ) AS t ON v.visit_id = t.visit_id
WHERE
    t.amount IS NULL
GROUP BY
    v.customer_id;