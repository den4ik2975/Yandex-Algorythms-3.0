n = int(input())
mtrx = [list(input()) for i in range(n)]
x, y = map(int, input().split())
var_i = [-1, 1, 0, 0]
var_j = [0, 0, -1, 1]
que = [(x - 1, y - 1)]
cnt = 1
visited = []

while que:
    cur = que[0]
    if cur not in visited:
        visited.append(cur)
        for i in range(4):
            hlp_i = var_i[i] + cur[0]
            hlp_j = var_j[i] + cur[1]
            if n > hlp_i >= 0 and n > hlp_j >= 0:
                if mtrx[hlp_i][hlp_j] == '.':
                    if (hlp_i, hlp_j) not in visited and (hlp_i, hlp_j) not in que:
                        que.append((hlp_i, hlp_j))
                        cnt += 1
    que.pop(0)

print(cnt)