def solution(myStr):
    arr = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ')
    if len(arr.split()) == 0 :
        return ["EMPTY"]
    return arr.split()