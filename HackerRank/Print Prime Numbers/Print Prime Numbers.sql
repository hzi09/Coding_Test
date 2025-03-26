WITH RECURSIVE numbers(n) AS (
    SELECT 2 
    UNION ALL
    SELECT n + 1 FROM numbers WHERE n < 1000
)
SELECT GROUP_CONCAT(n SEPARATOR '&') 
FROM numbers 
WHERE NOT EXISTS (
    SELECT 1 
    FROM numbers AS t 
    WHERE t.n < numbers.n AND numbers.n % t.n = 0
)