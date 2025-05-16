import sys

input = sys.stdin.readline
n = int(input())
opinions = [int(input()) for _ in range(n)]

def trim_round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

if n == 0:
    print(0)
else :
    opinions.sort()
    trim_cnt = trim_round(n*0.15)
    trimmed_opinions = opinions[trim_cnt:n-trim_cnt]
    avg = trim_round(sum(trimmed_opinions)/len(trimmed_opinions))
    print(avg)