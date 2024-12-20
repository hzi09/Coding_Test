def solution(lines):
    sets = [set(range(min(i),max(i))) for i in lines]
    line12 = sets[0] & sets[1]
    line23 = sets[1] & sets[2]
    line31 = sets[2] & sets[0]
    return len(line12 | line23 | line31)