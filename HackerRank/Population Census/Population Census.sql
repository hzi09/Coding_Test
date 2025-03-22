SELECT SUM(CI.Population)
FROM CITY CI JOIN COUNTRY CO ON CI.CountryCode = CO.Code
WHERE Continent LIKE 'Asia'