def solution(picture, k):
    answer = []
    for i in picture :
        pic_str = ''
        for j in i :
            pic_str += j*k
        for _ in range(k) :
            answer.append(pic_str)
    return answer