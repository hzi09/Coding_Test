SELECT person_name
FROM (SELECT *, SUM(weight) OVER(ORDER BY turn) AS 'total'
      FROM Queue)a
WHERE total <= 1000
ORDER BY total DESC
LIMIT 1