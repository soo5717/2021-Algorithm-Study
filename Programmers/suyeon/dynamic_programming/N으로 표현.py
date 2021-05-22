def solution(N, number):
    if N == number: return 1
    
    DP = [{}, { N }]
    for i in range(2, 9):
        temp = { int(str(N) * i) }
        
        for j in range(1, i // 2 + 1):
            for num_1 in DP[j]:
                for num_2 in DP[i - j]: 
                    temp.add(num_1 + num_2)
                    temp.add(num_1 - num_2)
                    temp.add(num_2 - num_1)
                    temp.add(num_1 * num_2)
                    if num_2: temp.add(num_1 // num_2)
                    if num_1: temp.add(num_2 // num_1)
                    
                    if number in temp: return i
                    
        DP.append(temp)
    return -1