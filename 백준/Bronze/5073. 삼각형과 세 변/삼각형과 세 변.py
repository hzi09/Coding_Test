while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0 :
        break

    if a == b == c :
        result = "Equilateral"
    elif a == b or b == c or a == c:
        if a + b <= c or a + c <= b or b + c <= a:
            result = "Invalid"
        else:
            result = "Isosceles"
    else:
        if a + b <= c or a + c <= b or b + c <= a:
            result = "Invalid"
        else:
            result = "Scalene"

    print(result)