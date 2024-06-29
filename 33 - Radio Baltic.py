import math

class Node:
    def __init__(self, num):
        self.num = num
        self.neighbors = []

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

distances = []
color = []

def dfs(v, c):
    color[v.num] = c
    for e in v.neighbors:
        if color[e.num] == 0:
            dfs(e, 3 - c)

def check(n, power):
    global distances, color
    color = [0] * n
    gr = [Node(i) for i in range(n)]
    for i in range(n):
        for j in range(i):
            if distances[i][j] < power:
                gr[i].neighbors.append(gr[j])
                gr[j].neighbors.append(gr[i])
    for i in range(n):
        if color[i] == 0:
            dfs(gr[i], 1)
    for i in range(n):
        for j in range(i):
            if distances[i][j] < power and color[i] == color[j]:
                return False
    return True

def find_dist(a, b):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

n = int(input())
distances = [[0]*n for _ in range(n)]
points = [Point(*map(float, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i):
        d = find_dist(points[i], points[j])
        distances[i][j] = d
        distances[j][i] = d

l, r, eps = 0, 100000.0, 0.00000001
while r - l > eps:
    m = (l + r) / 2
    if check(n, m):
        l = m
    else:
        r = m

check(n, l)
print("{:.8f}".format(r/2))
print(*color)
