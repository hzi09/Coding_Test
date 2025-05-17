WITH Buy_CTE AS (
    SELECT stock_name, price AS buy_price,
           ROW_NUMBER() OVER (PARTITION BY stock_name ORDER BY operation_day) AS rn
    FROM Stocks
    WHERE operation = 'Buy'
),
Sell_CTE AS (
    SELECT stock_name, price AS sell_price,
           ROW_NUMBER() OVER (PARTITION BY stock_name ORDER BY operation_day) AS rn
    FROM Stocks
    WHERE operation = 'Sell'
)
SELECT b.stock_name,
       SUM(s.sell_price - b.buy_price) AS capital_gain_loss
FROM Buy_CTE b
JOIN Sell_CTE s
  ON b.stock_name = s.stock_name AND b.rn = s.rn
GROUP BY b.stock_name