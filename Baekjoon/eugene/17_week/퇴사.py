if __name__ == "__main__":
    n = int(input())
    dp = [0]*(n+1)
    time, pay = [],[]
    
    for i in range(n):
        t, p = map(int, input().split())
        time.append(t)
        pay.append(p)

    for i in range(n-1, -1, -1):
        if time[i]+i > n :
             dp[i] = dp[i+1]
        else :
            dp[i] = max(dp[i+1], pay[i]+dp[i+time[i]]) 
    print(dp[0])
