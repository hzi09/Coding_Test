SELECT e.employee_id
FROM Employees e LEFT JOIN Employees m ON e.manager_id = m.employee_id
WHERE e.salary < 30000 AND m.employee_id IS NULL
ORDER BY 1