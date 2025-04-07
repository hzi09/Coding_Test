card = list(input().split('.'))

is_valid = True

for i in range(len(card)):
    if len(card[i]) % 2 == 1:
        is_valid = False
        break
    else:
        card[i] = 'AAAA' * (len(card[i]) // 4) + 'BB' * (len(card[i]) % 4 // 2)

if is_valid:
    print('.'.join(card))
else:
    print(-1)