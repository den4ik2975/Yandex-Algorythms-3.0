n, m = map(int, input().split())

mtrx = [[0] * m for i in range(n)]
mtrx[0][0] = 1 
var_i = [-1, -1, -2, -2, 1, 1, 2, 2]
var_j = [-2, 2, -1, 1, -2, 2, -1, 1]


for hlp_j in range(m):
    j = hlp_j
    i = 0
    while j >= 0 and i < n:
        if mtrx[i][j] != 0:
            for var in range(8):
                hlp_i = i + var_i[var]
                hlp_j = j + var_j[var]
                if n > hlp_i >= 0 and m > hlp_j >= 0:
                    mtrx[hlp_i][hlp_j] = mtrx[hlp_i][hlp_j] + mtrx[i][j]
        i += 1
        j -= 1

for hlp_i in range(1, n):
    j = m - 1
    i = hlp_i
    while j >= 0 and i < n:
        if mtrx[i][j] != 0:
            for var in range(8):
                hlp_i = i + var_i[var]
                hlp_j = j + var_j[var]
                if n > hlp_i >= 0 and m > hlp_j >= 0:
                    mtrx[hlp_i][hlp_j] = mtrx[hlp_i][hlp_j] + mtrx[i][j]
        i += 1
        j -= 1

print(mtrx[n - 1][m - 1])