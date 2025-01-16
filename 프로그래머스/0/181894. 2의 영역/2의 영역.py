def solution(arr):
    try:
        start = arr.index(2)
        end = len(arr) - 1 - arr[::-1].index(2)
        return arr[start:end + 1]
    except ValueError:
        return [-1]