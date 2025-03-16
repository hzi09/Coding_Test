# [Top Earners](https://www.hackerrank.com/challenges/earnings-of-employees/problem?isFullScreen=true)

## Easy, SQL (Basic)
We define an employee's total earnings to be their monthly $salary × months$ worked, and the maximum total earnings to be the maximum total earnings for any employee in the **Employee** table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as $2$ space-separated integers.

**Input Format**

The **Employee** table is described as follows:

![Image](https://github.com/user-attachments/assets/75253d56-d82b-45d6-89f9-4782598d3b07)

where employee_id is an employee's ID number, name is their name, months is the total number of months they've been working for the company, and salary is the their monthly salary.


**Sample Input**

![Image](https://github.com/user-attachments/assets/cfc924e0-1300-4c9d-9deb-892b0f0ebd34)

**Sample Output**

```
69952 1
```

**Explanation**

The table and earnings data is depicted in the following diagram:

![Image](https://github.com/user-attachments/assets/d6b3a3fc-0f19-49a1-995e-d65869b6a7fc)

The maximum earnings value is `69952`. The only employee with earnings = `69952 `is Kimberly, so we print the maximum earnings value (`69952`) and a count of the number of employees who have earned  `$69952`(which is `1`) as two space-separated values.