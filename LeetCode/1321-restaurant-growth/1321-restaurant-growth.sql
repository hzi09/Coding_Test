WITH DailyRevenue AS (
    SELECT visited_on, SUM(amount) AS amount
    FROM Customer
    GROUP BY visited_on
)
SELECT d1.visited_on, 
       SUM(d2.amount) AS amount,
       ROUND(SUM(d2.amount) / 7, 2) AS average_amount
FROM DailyRevenue d1 JOIN DailyRevenue d2 ON d2.visited_on BETWEEN d1.visited_on - INTERVAL 6 DAY AND d1.visited_on
GROUP BY d1.visited_on
HAVING COUNT(d2.visited_on) = 7
ORDER BY d1.visited_on


