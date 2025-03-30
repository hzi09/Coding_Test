def solution(order):
    wait_box = []
    current = 1
    idx = 0
    n = len(order)

    while current <= n :
        if order[idx] == current :
            idx += 1
            current += 1
        elif wait_box and wait_box[-1] == order[idx] :
            wait_box.pop()
            idx += 1
        else :
            wait_box.append(current)
            current += 1

    while wait_box and idx < n and wait_box[-1] == order[idx] :
        wait_box.pop()
        idx += 1

    return idx