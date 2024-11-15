while True:
    n = input()
    result = 0
    if n == '#':
        break
    for i in range(len(n)):
        if n[i] == "~":
            result += 8 ** (len(n) - 1 - i) * 0
        elif n[i] == "\\":
            result += 8 ** (len(n) - 1 - i) * 1
        elif n[i] == "(":
            result += 8 ** (len(n) - 1 - i) * 2
        elif n[i] == "@":
            result += 8 ** (len(n) - 1 - i) * 3
        elif n[i] == "?":
            result += 8 ** (len(n) - 1 - i) * 4
        elif n[i] == ">":
            result += 8 ** (len(n) - 1 - i) * 5
        elif n[i] == "&":
            result += 8 ** (len(n) - 1 - i) * 6
        elif n[i] == "%":
            result += 8 ** (len(n) - 1 - i) * 7
        elif n[i] == "/":
            result += 8 ** (len(n) - 1 - i) * -1
    print(result)