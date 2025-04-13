def count_ladders(N):
    dp = [[0] * (N + 2) for _ in range(N + 2)]
    dp[0][0] = 1
    for k in range(N + 1):
        for m in range(N, 0, -1):
            if m > k:
                dp[k][m] = 0
            else:
                dp[k][m] = dp[k - m][m + 1] + dp[k][m + 1]
    return dp[N][1]

N = int(input())
print(count_ladders(N))