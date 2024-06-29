n = int(input())
dp = [0] + [10 ** 8] * n

for i in range(1, n + 1):
  for j in range(1, n + 1):
    if j ** 3 > i:
      break
    dp[i] = min(dp[i], dp[i - (j * j * j)] + 1)

print(dp[n])
