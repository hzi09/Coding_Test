SELECT DISTINCT(CITY) AS CITY
FROM STATION
WHERE CITY NOT REGEXP '[aeiou]$'