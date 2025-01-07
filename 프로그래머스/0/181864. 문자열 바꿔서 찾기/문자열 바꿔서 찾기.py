def solution(myString, pat):
    myString = myString.replace('A', 'a').replace('B', 'b')
    pat = pat.replace('B', 'a').replace('A','b')
    return 1 if pat in myString else 0