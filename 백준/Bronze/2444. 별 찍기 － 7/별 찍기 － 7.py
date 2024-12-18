n = int(input())

star_num = 1

for i in range(1, 2*n) :
    if i < n :
        print(f'{" "*(n - i)}{"*" * star_num}')
        star_num += 2
    elif i == n :
        print(f'{"*" * star_num}')
    else :
        star_num -= 2
        print(f'{" "*(i-n)}{"*" * star_num}')