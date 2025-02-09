def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    weights = [781, 156, 31, 6, 1]
    answer = 0
    
    for idx, char in enumerate(word) :
        index = vowels.index(char)
        answer += index * weights[idx]+1
    return answer