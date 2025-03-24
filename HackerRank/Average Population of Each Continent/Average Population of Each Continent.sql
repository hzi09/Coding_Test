WITH Ordered AS (
    SELECT LAT_N, ROW_NUMBER() OVER (ORDER BY LAT_N) AS row_num,
                 COUNT(*) OVER () AS total_count
    FROM STATION
)
SELECT ROUND(
    CASE 
        WHEN total_count % 2 = 1 
        THEN (SELECT LAT_N FROM Ordered WHERE row_num = (total_count + 1) / 2)
        ELSE (SELECT AVG(LAT_N) FROM Ordered WHERE row_num IN (total_count / 2, total_count / 2 + 1))
        END, 4)
FROM Ordered
LIMIT 1;
