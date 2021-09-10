def get_number_of_cases():
    dp = [0] * (n + 2)  # n이 1일 때 인덱스 에러 방지
    dp[1], dp[2] = 1, 3
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10_007
    return dp[n]


if __name__ == '__main__':
    n = int(input())
    print(get_number_of_cases())