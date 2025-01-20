def solution(arr):
    rows, cols = len(arr), len(arr[0])
    if rows > cols:
        for i in range(rows):
            arr[i] += [0] * (rows - cols)
    elif rows < cols:
        for _ in range(cols - rows):
            arr.append([0] * cols) 
    return arr