def solution(brown, yellow):
    answer = []
    for i in range(3, brown//2):
        if (brown//2-i)*(i-2) == yellow:
            return [brown//2+2-i,i]
