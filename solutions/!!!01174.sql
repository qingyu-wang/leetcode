-- 1174. Immediate Food Delivery II
-- https://leetcode.com/problems/immediate-food-delivery-ii/description/

SELECT
    ROUND(AVG(CASE WHEN t.immediate THEN 100 ELSE 0 END), 2) AS immediate_percentage
FROM
    (
        SELECT
            t1.order_date=MIN(t2.customer_pref_delivery_date) AS immediate
        FROM
            (
                SELECT
                    customer_id,
                    MIN(order_date) AS order_date
                FROM
                    Delivery
                GROUP BY
                    customer_id
            ) AS t1
            LEFT JOIN Delivery AS t2 ON 
                t1.customer_id = t2.customer_id
                AND t1.order_date = t2.order_date
        GROUP BY
            t1.customer_id
    ) AS t;