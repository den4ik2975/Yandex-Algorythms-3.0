n, a, b = map(int, input().split())

dp = [0] + [0] + [max(a, b)] + [0] * (n - 2)

for i in range(1, n + 1):
    var = []
    for j in range(1, i):
        var.append(max(dp[j] + a, dp[i - j] + b))
    if var:
        dp[i] = min(var)

print(dp[n])