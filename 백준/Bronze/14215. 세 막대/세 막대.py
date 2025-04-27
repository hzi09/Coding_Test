line = list(map(int, input().split()))

line.sort()

if line[0] + line[1] > line[2]:
    result = sum(line)
else :
    result = (line[0] + line[1]) * 2 - 1

print(result)
