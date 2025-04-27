angle = [int(input()) for _ in range(3)]

if sum(angle) == 180:
    if angle[0] == angle[1] == angle[2] ==60:
        result = "Equilateral"
    elif angle[0] == angle[1] or angle[1] == angle[2] or angle[0] == angle[2]:
        result = "Isosceles"
    else:
        result = "Scalene"
else:
    result = "Error"

print(result)
