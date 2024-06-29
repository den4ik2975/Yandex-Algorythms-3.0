import sys

sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val
        self.visited = False

n, m = map(int, input().split())
mat = []
field = [[None]*m for _ in range(n)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(v):
    field[v.x][v.y].visited = True
    for i in range(4):
        x = min(max(v.x + di[i], 0), n - 1)
        y = min(max(v.y + dj[i], 0), m - 1)
        if field[x][y].val >= v.val and not field[x][y].visited:
            dfs(field[x][y])

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        node = Node(i, j, row[j])
        mat.append(node)
        field[i][j] = node

mat.sort(key=lambda x: (x.val, x.x, x.y))
cnt = 0
for v in mat:
    if not field[v.x][v.y].visited:
        cnt += 1
        dfs(v)

print(cnt)
