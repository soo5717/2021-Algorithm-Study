def solution(N, number):
    if N == number: return 1

    DP = [{}, { N }]
    for i in range(2, 9):
        temp = { int(str(N) * i) }

        for j in range(1, i//2 + 1):
            for x in DP[j]:
                for y in DP[i - j]:
                    temp.add(x + y)
                    temp.add(x - y)
                    temp.add(x - y)
                    temp.add(x * y)
                    if y: temp.add(x // y)
                    if x: temp.add(y // x)

                    if number in temp: return i
        DP.append(temp)
    return -1
