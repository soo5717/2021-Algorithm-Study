if __name__ == "__main__":
    first = input()
    second = input()

    len_first = len(first)
    len_second = len(second)
    
    LCS = [[0]*(len_first+1) for _ in range(len_second+1)]
    for i in range(1, len_second+1) : #1~3
        for j in range(1, len_first+1) : #1~2
            if first[j-1] == second[i-1] :
                LCS[i][j] = LCS[i-1][j-1]+1
            else :
                LCS[i][j] = max(LCS[i][j-1], LCS[i-1][j])

    print(LCS[-1][-1])
