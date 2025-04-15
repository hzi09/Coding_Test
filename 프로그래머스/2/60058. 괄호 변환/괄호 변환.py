def solution(p):
    def split_uv(w):
        left, right = 0, 0
        for i in range(len(w)):
            if w[i] == '(':
                left += 1
            else:
                right += 1
            if left == right:
                u = w[:i+1]
                v = w[i+1:]
                return u, v

    def is_correct(u):
        stack = []
        for ch in u:
            if ch == '(':
                stack.append(ch)
            else:
                if not stack:
                    return False
                stack.pop()
        return True

    if p == '':
        return ''

    u, v = split_uv(p)

    if is_correct(u):
        return u + solution(v)
    else:
        temp = '('
        temp += solution(v)
        temp += ')'
        flipped = ''
        for ch in u[1:-1]:
            if ch == '(':
                flipped += ')'
            else:
                flipped += '('
        temp += flipped
        return temp
