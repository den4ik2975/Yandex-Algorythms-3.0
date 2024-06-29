n, m = map(int, input().split())
graph = {i: [] for i in range(n)}
for i in range(m):
    x, y = map(int, input().split())
    graph[y - 1].append(x - 1)

visited = [0]
stack = [0]

while stack:
    cur = stack[0]
    stack.pop(0)
    for i in graph[cur]:
        if i not in visited:
            visited.append(i)
            stack = [i] + stack

for i in sorted(visited):
    print(i + 1, end=' ')