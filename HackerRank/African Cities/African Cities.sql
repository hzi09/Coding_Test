SELECT CI.Name
FROM CITY CI JOIN COUNTRY CO ON CI.CountryCode = CO.Code
WHERE Continent LIKE 'Africa'