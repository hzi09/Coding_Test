fb_list = [input() for _ in range(3)]

for i in fb_list :
    if i.isdigit() :
        fb_id = fb_list.index(i)
        if fb_id == 0 :
            answer = int(i)+3
        elif fb_id == 1 :
            answer = int(i)+2
        else :
            answer = int(i)+1
        break

if answer % 3 == 0 and answer % 5 ==0 :
    print('FizzBuzz')
elif answer % 5 ==0 :
    print('Buzz')
elif answer % 3 == 0 :
    print('Fizz')
else :
    print(answer)