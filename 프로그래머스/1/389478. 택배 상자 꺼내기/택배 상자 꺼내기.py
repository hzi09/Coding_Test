def solution(n, w, num):
    y, x = divmod(num-1, w)

    if y % 2 == 1 :
        x = w - 1 - x

    cnt = 0

    for i in range(y+1, (n + w - 1) // w) :
        if i % 2 == 0 :
            target_x = x
        else :
            target_x = w - 1 - x

        box_num = i * w + target_x + 1
        if box_num <= n :
            cnt += 1

    return cnt + 1