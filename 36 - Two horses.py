from string import ascii_lowercase
from collections import deque

asci = ascii_lowercase
pos = input().split()
red_pos = (asci.index(pos[0][0]), int(pos[0][1]) - 1)
green_pos = (asci.index(pos[1][0]), int(pos[1][1]) - 1)

que = deque([(red_pos, 0)])
visited = {red_pos}

while que:
    pos, distance = que.popleft()
    if pos == green_pos:
        if distance % 2 == 0:
            print(distance // 2)
        else:
            print(-1)
        exit()
    moves = []
    x, y = pos
    for dx, dy in [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx <= 7 and 0 <= ny <= 7:
            moves.append((nx, ny))
    for move in moves:
        if move not in visited:
            visited.add(move)
            que.append((move, distance + 1))
print(-1)

