import math

def solution(brown, yellow):
    answer = []
    for i in range(3, int(math.sqrt(brown+yellow))+1):
        if (brown+yellow) % i == 0:
            a = int((brown+yellow) // i)
            b = i
            if (a-2)*(b-2) == yellow:
                break
    return [a, b]