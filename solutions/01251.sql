-- 1251. Average Selling Price
-- https://leetcode.com/problems/average-selling-price/description/

SELECT
    p.product_id,
    ROUND(COALESCE(SUM(p.price * u.units) / SUM(u.units), 0), 2) AS average_price
FROM
    Prices AS p
    LEFT JOIN UnitsSold AS u ON 
        p.product_id = u.product_id
        AND p.start_date <= u.purchase_date
        AND p.end_date >= u.purchase_date
GROUP BY
    p.product_id;