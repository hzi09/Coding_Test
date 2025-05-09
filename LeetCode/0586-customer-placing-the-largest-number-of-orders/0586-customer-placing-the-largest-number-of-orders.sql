SELECT customer_number
FROM (
    SELECT customer_number, COUNT(*) AS order_count
    FROM Orders
    GROUP BY 1
) AS customer_counts
ORDER BY order_count DESC
LIMIT 1