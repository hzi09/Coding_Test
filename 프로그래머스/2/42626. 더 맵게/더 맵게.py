import heapq

def solution(scoville, K) :
    answer = 0
    s = scoville
    heapq.heapify(s)
    while s and s[0] < K:
        try:
            new_food = heapq.heappop(s) + heapq.heappop(s) * 2
            heapq.heappush(s, new_food)
            answer += 1
        except:
            return -1
    return answer