n = int(input())

dp = [[1, 0, 0]]
ans = 0
cnt = 0
for i in range(2, n + 1):
    fr = dp[-1][0] + (2 * i) - 1
    sc = dp[-1][1] + (i - 1)
    th = 0
    if i > 3:
        if i % 2 == 0:
            th = dp[-1][2] + cnt + 1
            cnt += 1
        else:
            th = dp[-1][2] + cnt
    ans += sc + th
    dp.append([fr, sc, th])

print(ans + dp[-1][0])
