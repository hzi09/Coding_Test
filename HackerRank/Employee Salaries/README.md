# [Employee Salaries](https://www.hackerrank.com/challenges/salary-of-employees/problem?isFullScreen=true)

## Easy, SQL (Basic)
Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater than $2000 per month who have been employees for less than 10 months. Sort your result by ascending employee_id.

**Input Format**

The Employee table containing employee data for a company is described as follows:

![Image](https://github.com/user-attachments/assets/5ad6afa9-94e5-4b53-aa58-4b696bb27cde)

where employee_id is an employee's ID number, name is their name, months is the total number of months they've been working for the company, and salary is their monthly salary.

**Sample Input**

![Image](https://github.com/user-attachments/assets/93cee0fa-18a8-430f-a0bf-d8ccc3d8e985)


**Sample Output**

```
Angela
Michael
Todd
Joe
```

**Explanation**

Angela has been an employee for 1 month and earns $3443 per month.

Michael has been an employee for 6 months and earns $2017 per month.

Todd has been an employee for 5 months and earns $3396 per month.

Joe has been an employee for 9 months and earns $3573 per month.

We order our output by ascending employee_id.