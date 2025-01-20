def solution(arr):
    if len(arr) > len(arr[0]) :
        for i in range(len(arr)) :
            arr[i] += [0] * (len(arr)-len(arr[-1]))
    elif len(arr) < len(arr[0]) :
        for i in range(len(arr[0])-len(arr)) :
            arr.append([0] * len(arr[0]))
    return arr