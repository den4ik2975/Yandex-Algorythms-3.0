n = int(input())

programs = [0]
dp = [0] * 32402
delta = 9 * 3600
h = set()
last_a = 0
last_t = 0
for i in range(n):
    a, t = input().split()
    a = list(map(int, a.split(':')))
    a = a[0] * 3600 + a[1] * 60 + a[2]
    programs += [last_t] * (a - last_a)
    last_a = a
    last_t = int(t)
programs += [last_t] * (64801 - last_a)

for i in range(1, 14402):
    dp[i] = max(dp[i - 1], dp[i])
    t = programs[i + delta]
    if i + t <= 14401:
        dp[i + t] = max(dp[i] + 1, dp[i + t])

dp[18001] = dp[14401]
for i in range(18001, 32402):
    dp[i] = max(dp[i - 1], dp[i])
    t = programs[i + delta]
    if i + t <= 32401:
        dp[i + t] = max(dp[i] + 1, dp[i + t])


print(dp[-1])



