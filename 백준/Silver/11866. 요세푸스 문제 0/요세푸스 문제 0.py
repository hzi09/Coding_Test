n, k = map(int, input().split())

queue = [i for i in range(1, n+1)]
answer = []
current = 0

while queue:
    current = (current + k - 1) % len(queue)
    answer.append(queue.pop(current))

print("<" + ", ".join(map(str, answer)) + ">")
