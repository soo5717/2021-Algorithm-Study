def solution(brown, yellow):
    answer = []
    sum = brown+yellow

    for i in range(3, (sum)**0.5+1):
        if (sum) % i == 0:
            if (sum//i-2)*(i-2) == yellow:
                return [sum//i, i]