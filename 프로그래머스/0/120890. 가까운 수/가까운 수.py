def solution(array, n):
    offset = []
    for i in array :
        offset.append(abs(n - i))
    if offset.count(min(offset)) == 1 :
        answer = array[offset.index(min(offset))]
    else :
        min_num = (x for x, value in enumerate(offset) if value == min(offset))
        min_num_list = []
        for j in min_num :
            min_num_list.append(array[j])
        answer = min(min_num_list)
    return answer