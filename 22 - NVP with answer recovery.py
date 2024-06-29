ln = int(input())
lst = list(map(int, input().split()))
dp, ind = ([1] + [0] * (ln - 1)), [-1] * ln

for i in range(1, ln):
    cur = lst[i]
    maxx = 0
    indd = -1
    for j in range(i):
        if cur > lst[j]:
            if dp[j] > maxx:
                maxx = dp[j]
                indd = j
    dp[i] = maxx + 1
    ind[i] = indd
ans = []
mx = max(dp)
for i in range(ln - 1, -1, -1):
    if dp[i] == mx:
        ans = [lst[i]]
        nextt = ind[i]
        while nextt >= 0:
            ans = [lst[nextt]] + ans
            nextt = ind[nextt]

print(*ans)