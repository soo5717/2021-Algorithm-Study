def solution(brown, yellow):
    answer = []
    round2 = brown//2
    for i in range(3, round2):
        if (round2-i)*(i-2) == yellow:
            return [round2+2-i,i]
