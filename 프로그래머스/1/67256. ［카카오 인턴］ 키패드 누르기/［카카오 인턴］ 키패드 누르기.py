def solution(numbers, hand):
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    l_hand = keypad['*']
    r_hand = keypad['#']
    answer = ''
    
    for num in numbers :
        if num in [1, 4, 7] :
            answer += 'L'
            l_hand = keypad[num]
        elif num in [3, 6, 9] :
            answer += 'R'
            r_hand = keypad[num]
        else :
            l_dist = abs(l_hand[0] - keypad[num][0]) + abs(l_hand[1] - keypad[num][1])
            r_dist = abs(r_hand[0] - keypad[num][0]) + abs(r_hand[1] - keypad[num][1])
            
            if l_dist < r_dist :
                answer += 'L'
                l_hand = keypad[num]
            elif l_dist > r_dist :
                answer += 'R'
                r_hand = keypad[num]
            else :
                if hand == 'left' :
                    answer += 'L'
                    l_hand = keypad[num]
                elif hand == 'right' :
                    answer += 'R'
                    r_hand = keypad[num]
            
    return answer