def solution(brown, yellow):
    answer = []
    half_round = brown//2   
    for i in range(3, half_round):
        if (half_round-i)*(i-2) == yellow:
            return [half_round+2-i,i]
