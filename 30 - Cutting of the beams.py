l, n = map(int, input().split())
ras = [0] + list(map(int, input().split())) + [l]
n += 2

dp = [[0] * n for _ in range(n)]


for h in range(n - 1, -1, -1):
    for i in range(h):
        j = i + (n - h)
        hlp = []
        for k in range(i + 1, j):
            hlp.append(dp[i][k] + dp[k][j])
        dp[i][j] = abs(ras[j] - ras[i]) + (min(hlp) if hlp else 0)

print(dp[0][n - 1] - l)