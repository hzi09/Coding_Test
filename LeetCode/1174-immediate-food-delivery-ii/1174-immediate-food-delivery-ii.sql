SELECT ROUND(SUM(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) / COUNT(*)*100, 2) AS immediate_percentage
FROM Delivery
WHERE order_date = (SELECT MIN(d2.order_date)
                    FROM Delivery d2
                    WHERE d2.customer_id = Delivery.customer_id)