SELECT CONCAT(name, '(', LEFT(occupation, 1), ')') AS output
FROM OCCUPATIONS

UNION ALL

SELECT CONCAT('There are a total of ', COUNT(*), ' ', LOWER(occupation), 's.') AS output
FROM OCCUPATIONS
GROUP BY occupation
ORDER BY output