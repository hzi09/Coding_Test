from collections import Counter

def solution(k, tangerine):
    count = Counter(tangerine)
    sorted_counts = sorted(count.values(), reverse=True)
    total = 0
    kinds = 0

    for c in sorted_counts:
        total += c
        kinds += 1
        if total >= k:
            return kinds

    return kinds