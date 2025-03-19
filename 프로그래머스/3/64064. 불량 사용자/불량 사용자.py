import re
from itertools import permutations

def solution(user_id, banned_id):
    banned_id = [f"^{b.replace('*', '.')}$" for b in banned_id]
    
    answer = []
    for b in banned_id :
        select = [user for user in user_id if re.match(b, user)]
        answer.append(select)

    answer_set = set()
    for p in permutations(user_id, len(banned_id)):
        if all(re.match(banned_id[i], p[i]) for i in range(len(banned_id))) :
            answer_set.add(frozenset(p))
    return len(answer_set)