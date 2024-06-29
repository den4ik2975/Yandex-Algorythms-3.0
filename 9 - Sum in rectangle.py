n, m, k = map(int, input().split())
matrix = []
pref = []
for i in range(n):
    matrix += [list(map(int, input().split()))]
    pref += [[0] * m]


pref[0][0] = matrix[0][0]
for i in range(1, n):
    pref[i][0] = pref[i - 1][0] + matrix[i][0]
for i in range(1, m):
    pref[0][i] = pref[0][i - 1] + matrix[0][i]
for i in range(1, n):
    for j in range(1, m):
        pref[i][j] = pref[i - 1][j] + pref[i][j - 1] - pref[i - 1][j - 1] + matrix[i][j]

for req in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
    if x1 - 1 < 0 and y1 - 1 < 0:
        cnt = pref[x2][y2]
    elif x1 - 1 < 0:
        cnt = pref[x2][y2] - pref[x2][y1 - 1]
    elif y1 - 1 < 0:
        cnt = pref[x2][y2] - pref[x1 - 1][y2]
    else:
        cnt = pref[x2][y2] - pref[x1 - 1][y2] - pref[x2][y1 - 1] + pref[x1 - 1][y1 - 1]

    print(cnt)