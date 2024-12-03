n = list(map(int, input().split()))
s = list(range(1,9))

if n == s :
    print('ascending')
elif n == list(reversed(s)) :
    print('descending')
else :
    print('mixed')