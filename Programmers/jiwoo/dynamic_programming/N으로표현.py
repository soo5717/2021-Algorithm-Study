def solution(N, number):
    if N == number:
        return 1

    S = [{}, {N}]

    for i in range(2, 9):
        temp = {int(str(N) * i)}
        for j in range(1, i//2 + 1):
            for a in S[j]:
                for b in S[i-j]:
                    temp.add(a+b)
                    temp.add(a-b)
                    temp.add(b-a)
                    temp.add(a*b)
                    if b:
                        temp.add(a//b)
                    if a:
                        temp.add(b//a)
                    if number in temp:
                        return i
        S.append(temp)
            
    return -1