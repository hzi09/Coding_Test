SELECT name
FROM Employee e LEFT JOIN (SELECT managerId, COUNT(*) AS cnt
                           FROM Employee
                           GROUP BY managerId)c ON e.id = c.managerId
WHERE cnt >= 5