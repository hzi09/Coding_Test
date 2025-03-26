def solution(id_list, report, k):
    report = list(set(report))
    
    id_dict = {user: 0 for user in id_list}
    
    reposter_id = {user: set() for user in id_list}
    
    for r in report:
        reporter, reported = r.split()
        if reported not in reposter_id[reporter]:
            reposter_id[reporter].add(reported)
            id_dict[reported] += 1
    
    block = {user for user, count in id_dict.items() if count >= k}
    
    answer = [0] * len(id_list)
    for idx, uid in enumerate(id_list):
        answer[idx] = sum(1 for reported in reposter_id[uid] if reported in block)    
    return answer
