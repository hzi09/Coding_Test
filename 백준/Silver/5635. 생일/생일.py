n = int(input())
students = {}

for i in range(n):
    name, day, month, year = input().split()
    students[name] = int(''.join([year.zfill(4), month.zfill(2), day.zfill(2)]))

print(max(students, key=students.get))
print(min(students, key=students.get))
