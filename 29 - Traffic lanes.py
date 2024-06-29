m, n = map(int, input().split())

dp = [[0] * m for _ in range(n)]
dp[0] = [1] * m

for j in range(n):
    dp[j][0] = 1

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1] + dp[i - 1][j - 1]

print(dp[n - 1][m - 1])
