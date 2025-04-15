n = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

def dfs(depth, total, plus, minus, multiply, divide):
    global min_result, max_result
    if depth == n:
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return
    
    if plus > 0:
        dfs(depth + 1, total + numbers[depth], plus - 1, minus, multiply, divide)
    if minus > 0:
        dfs(depth + 1, total - numbers[depth], plus, minus - 1, multiply, divide)
    if multiply > 0:
        dfs(depth + 1, total * numbers[depth], plus, minus, multiply - 1, divide)
    if divide > 0:
        dfs(depth + 1, int(total / numbers[depth]), plus, minus, multiply, divide - 1)

min_result = float('inf')
max_result = float('-inf')

dfs(1, numbers[0], operators[0], operators[1], operators[2], operators[3])

print(max_result)
print(min_result)