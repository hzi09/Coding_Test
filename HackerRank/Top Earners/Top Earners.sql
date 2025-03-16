SELECT MAX(total_earnings) AS max_earnings, COUNT(*) AS employee_count
FROM (
    SELECT salary * months AS total_earnings
    FROM Employee
) AS earnings_table
WHERE total_earnings = (
    SELECT MAX(salary * months) 
    FROM Employee)