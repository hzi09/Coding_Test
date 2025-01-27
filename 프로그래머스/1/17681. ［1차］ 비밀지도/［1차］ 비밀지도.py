def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    for i in range(n) :
        map1.append(str(bin(arr1[i])[2:]).zfill(n))
        map2.append(str(bin(arr2[i])[2:]).zfill(n))
        
        answer_n = ''
        for j in range(n) :
            if map1[i][j] == '1' or map2[i][j] == '1' :
                answer_n += '#'
            elif map1[i][j] == '0' or map2[i][j] == '0' :
                answer_n += ' '
        answer.append(answer_n)
    return answer