from heapq import *

n = int(input())
in_vert = [0] * n
graph = {}
heap = []
order = []
heapify(heap)
for i in range(n):
    graph[i] = []
    for j in list(map(lambda x: int(x) - 1, input().split()))[1:]:
        graph[i].append(j)
        in_vert[j] += 1

for i in range(n):
    if in_vert[i] == 0:
        heappush(heap, -i)

while heap:
    cur = abs(heappop(heap))
    order.append(cur)
    for i in graph[cur]:
        in_vert[i] -= 1
        if not in_vert[i]:
            heappush(heap, -i)
    graph[cur].clear()

for i in order[::-1]:
    print(i + 1, end=' ')