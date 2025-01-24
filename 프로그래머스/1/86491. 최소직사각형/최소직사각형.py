def solution(sizes):
    new_sizes = [sorted(i) for i in sizes]
    return max([i[0] for i in new_sizes]) * max([i[1] for i in new_sizes])