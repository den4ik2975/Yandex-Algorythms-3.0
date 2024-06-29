from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def tilt(maze, x, y, direction):
    dx, dy = directions[direction]
    nx, ny = x + dx, y + dy
    while 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != 1:
        x, y = nx, ny
        nx, ny = x + dx, y + dy
        if maze[x][y] == 2:
            return None
    return (x, y, direction)


start_state = (0, 0, -1)
visited = set([start_state])
queue = deque([(start_state, 0)])

while queue:
    state, steps = queue.popleft()
    x, y, direction = state
    for new_direction in range(4):
        if new_direction != direction:
            new_state = tilt(maze, x, y, new_direction)
            if new_state is not None and new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, steps + 1))
                if maze[new_state[0]][new_state[1]] == 2:
                    print(steps + 1)
                    exit()
            elif new_state is None:
                print(steps + 1)
                exit()
