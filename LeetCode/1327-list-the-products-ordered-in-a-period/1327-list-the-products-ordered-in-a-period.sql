SELECT product_name, SUM(o.unit) AS unit
FROM Products p JOIN Orders o ON p.product_id = o.product_id
WHERE order_date BETWEEN '2020-02-01' AND '2020-02-28'
GROUP BY 1
HAVING unit >= 100