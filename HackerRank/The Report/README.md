# [The Report](https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true)

## Medium, SQL (Intermediate)
You are given two tables: Students and Grades. Students contains three columns ID, Name and Marks.

![Image](https://github.com/user-attachments/assets/9af5a9bc-16dc-4f7c-9c6d-4962f01c5824)

Grades contains the following data:

![Image](https://github.com/user-attachments/assets/d63ad3e6-a45d-4fd4-9752-e06a615d4bd9)

Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. Ketty doesn't want the NAMES of those students who received a grade lower than 8. The report must be in descending order by grade -- i.e. higher grades are entered first. If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.

Write a query to help Eve.


**Sample Input**

![Image](https://github.com/user-attachments/assets/c3fc1541-482a-482a-9be7-771695c93f62)

**Sample Output**
```
Maria 10 99
Jane 9 81
Julia 9 88 
Scarlet 8 78
NULL 7 63
NULL 7 68
```

**Note**

Print "NULL"  as the name if the grade is less than 8.

**Explanation**

Consider the following table with the grades assigned to the students:

![Image](https://github.com/user-attachments/assets/a98d3867-a46a-45ee-b6c7-db4733a86f88)

So, the following students got 8, 9 or 10 grades:

- Maria (grade 10)
- Jane (grade 9)
- Julia (grade 9)
- Scarlet (grade 8)