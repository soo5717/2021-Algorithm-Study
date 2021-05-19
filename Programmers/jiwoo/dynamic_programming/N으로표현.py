def solution(N, number):
    if N == number:
        return 1

    S = [set() for i in range(8)]

    for i in range(8):
        S[i].add(int(str(N) * (i+1)))
        
    for i in range(1, len(S)):
        for j in range(i):
            for a in S[j]:
                for b in S[i-j-1]:
                    S[i].add(a+b)
                    S[i].add(a-b)
                    S[i].add(a*b)
                    if b != 0:
                        S[i].add(a//b)
        if number in S[i]:
            return i+1
            
    return -1