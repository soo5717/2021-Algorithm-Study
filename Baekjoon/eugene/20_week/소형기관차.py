if __name__ =="__main__":
    n = int(input())
    people = list(map(int, input().split()))
    max_n = int(input())

    S=[0]
    sum_val = 0

    for p in people:
        sum_val += p
        S.append(sum_val)

    dp = [[0] *(n+1) for _ in range(4)]

    for x in range(1,4):
        for y in range(x*max_n, n+1):
            if x == 1:
                dp[x][y] = max(dp[x][y-1], S[y]-S[y-max_n])
            else :
                dp[x][y] = max(dp[x][y-1], dp[x-1][y-max_n] + S[y]-S[y-max_n])
    print(dp[-1][-1])
