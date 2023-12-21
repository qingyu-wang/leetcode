-- 1327. List the Products Ordered in a Period
-- https://leetcode.com/problems/list-the-products-ordered-in-a-period/description/

SELECT
    p.product_name,
    SUM(o.unit) AS unit
FROM
    Products p
    INNER JOIN Orders o ON P.product_id = o.product_id
WHERE
    order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY
    p.product_name
HAVING
    SUM(o.unit) >= 100;

--

SELECT
    p.product_name,
    SUM(o.unit) AS unit
FROM
    Orders AS o
    LEFT JOIN Products AS p ON o.product_id = p.product_id
WHERE
    order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY
    p.product_name
HAVING
    SUM(o.unit) >= 100;