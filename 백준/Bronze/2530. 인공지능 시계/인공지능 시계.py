h, m, s = map(int, input().split())
d = int(input())

s_n, s_re = divmod(s + d, 60)
m_n, m_re = divmod(s_n + m, 60)

if h+m_n >= 24:
    h = (h + m_n) % 24
else :
    h = h + m_n

print(h, m_re, s_re)