from collections import Counter

def solution(str1, str2):
    str1_list = [str1.lower()[i:i+2] for i in range(0, len(str1)-1) if str1[i].isalpha() and str1[i+1].isalpha()]
    str2_list = [str2.lower()[i:i+2] for i in range(0, len(str2)-1) if str2[i].isalpha() and str2[i+1].isalpha()]
    
    counter1 = Counter(str1_list)
    counter2 = Counter(str2_list)
    
    inter = len(list((counter1 & counter2).elements()))
    union = len(list((counter1 | counter2).elements()))
    
    if inter == 0 and union == 0 :
        return 65536
    else :
        return int(inter / union * 65536)