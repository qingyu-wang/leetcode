-- 1164. Product Price at a Given Date
-- https://leetcode.com/problems/product-price-at-a-given-date/description/

WITH CTE AS (
    SELECT
        *,
        RANK() OVER (PARTITION BY product_id ORDER BY change_date DESC) AS r
    FROM
        Products
    WHERE
        change_date <= '2019-08-16'
)

SELECT
    product_id,
    new_price AS price
FROM
    CTE
WHERE
    r = 1

UNION

SELECT
    product_id,
    10 AS price
FROM
    Products
WHERE
    product_id NOT IN (
        SELECT product_id FROM cte
    );

--

SELECT
    DISTINCT product_id,
    10 AS price
FROM
    Products
WHERE
    product_id NOT IN (
        SELECT
            DISTINCT product_id
        FROM
            Products
        WHERE
            change_date <= '2019-08-16'
    )

UNION

SELECT
    product_id,
    new_price AS price
FROM
    Products
WHERE
    (product_id, change_date) IN (
        SELECT
            product_id,
            MAX(change_date) AS date
        FROM
            Products
        WHERE
            change_date <='2019-08-16'
        GROUP BY product_id
    );

--

SELECT
    DISTINCT p1.product_id,
    CASE WHEN p2.change_date IS NULL THEN 10 ELSE p1.new_price END AS price
FROM
    Products AS p1
    LEFT JOIN (
        SELECT
            product_id,
            MAX(change_date) AS change_date
        FROM
            Products
        WHERE
            change_date <= '2019-08-16'
        GROUP BY
            product_id
    ) AS p2 ON p1.product_id = p2.product_id
WHERE
    p1.change_date = p2.change_date
    OR p2.change_date is NULL;