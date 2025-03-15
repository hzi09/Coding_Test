# [The Blunder](https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=true)

## Easy, SQL (Basic)
Samantha was tasked with calculating the average monthly salaries for all employees in the **EMPLOYEES** table, but did not realize her keyboard's 0 key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

Write a query calculating the amount of error (i.e.: $actual-miscalcilated$ average monthly salaries), and round it up to the next integer.

**Input Format**

The **EMPLOYEES** table is described as follows:

![Image](https://github.com/user-attachments/assets/bf3b4686-68bc-4717-b751-7acb32550932)

**Note**: Salary is per month.

**Constraints**

$1000 < Salary < 10^5$.

**Sample Input**

![Image](https://github.com/user-attachments/assets/700ec09d-24bc-4b72-bd3a-9db0e6244d35)

**Sample Output**

```
2061
```

**Explanation**

The table below shows the salaries without zeros as they were entered by Samantha:

![Image](https://github.com/user-attachments/assets/e202427d-e370-4618-8e15-7d6d7613b7fd)

Samantha computes an average salary of `98.00`. The actual average salary is `2459.00`.

The resulting error between the two calculations is `2459.00 - 98.00 = 2061.00`. Since it is equal to the integer `2061`, it does not get rounded up.