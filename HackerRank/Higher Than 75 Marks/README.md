# [Higher Than 75 Marks](https://www.hackerrank.com/challenges/more-than-75-marks/problem?isFullScreen=true)

## Easy, SQL (Basic)
Query the Name of any student in STUDENTS who scored higher than 75 Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.

**Input Format**

The STUDENTS table is described as follows:

![Image](https://github.com/user-attachments/assets/a089acc8-2425-4797-8dd0-463faef8ff41)

The Name column only contains uppercase(A-Z) and lowercase(a-z) letters.

**Sample Input**

![Image](https://github.com/user-attachments/assets/803e3db8-1323-402a-81e6-13a77ea9aeeb)


**Sample Output**

```
Ashley
Julia
Belvet
```

**Explanation**

Only Ashley, Julia, and Belvet have *Marks* > 75. If you look at the last three characters of each of their names, there are no duplicates and 'ley' < 'lia' < 'vet'.