SELECT name
FROM SalesPerson
WHERE name NOT IN (SELECT sp.name
                    FROM SalesPerson sp
                        INNER JOIN Orders o
                            ON sp.sales_id = o.sales_id
                        INNER JOIN Company c
                            ON o.com_id = c.com_id
                    WHERE c.com_id = 1)