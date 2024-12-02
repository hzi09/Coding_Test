def solution(emergency):
    oder = []
    emergency_s = sorted(emergency, reverse= True)

    for i in emergency :
        oder.append(emergency_s.index(i)+1)
    return oder