def solution(hp):
    x = hp // 5
    y = (hp - (x*5)) // 3
    z = (hp - (x*5) - (y*3))
    return (x+y+z)