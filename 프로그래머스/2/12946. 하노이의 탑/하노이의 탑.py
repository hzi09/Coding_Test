def solution(n):
    stack = [(n, 1, 3, 2)]
    result = []
    call_stack = []

    while stack:
        curr_n, start, end, via = stack.pop()
        if curr_n == 1:
            result.append([start, end])
        else:
            stack.append((curr_n - 1, via, end, start))
            stack.append((1, start, end, via))
            stack.append((curr_n - 1, start, via, end))
    return result
