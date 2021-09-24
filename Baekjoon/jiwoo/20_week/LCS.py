S1 = input()
S2 = input()

count_s1 = len(S1) + 1
count_s2 = len(S2) + 1

LCS = [[0] * (count_s1) for _ in range(count_s2)]

for i in range(1, count_s2):
    for j in range(1, count_s1):
        if S1[j-1] == S2[i-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[-1][-1])