def solution(skill, skill_trees):
    skills = []
    for skill_tree in skill_trees :
        skills.append("".join(filter(lambda x: x in skill, skill_tree)))
    
    cnt = 0
    for s in skills :
        if skill.startswith(s) :
            cnt += 1
    return cnt