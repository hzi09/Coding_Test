SELECT x, y, z,
       CASE WHEN ABS(x) + ABS(y) > ABS(z) THEN 'Yes'
            ELSE 'No' END AS 'triangle'
FROM Triangle