from heapq import *

n, k, p = map(int, input().split())
req = [[int(input()), 0] for i in range(p)]
hlp = [p] * n
cnt = 0
heap = []
heapify(heap)
heap_set = set()


for i in range(p - 1, -1, -1):
    l = req[i][0]
    req[i] = [l, hlp[l - 1]]
    hlp[l - 1] = i

for i in req:
    flag = True
    num = i[0]
    if num in heap_set:
        k += 1
        cnt -= 1
    if len(heap) == k:
        rem = heappop(heap)
        heap_set.remove(rem[1])
    heappush(heap, [-i[1], i[0]])
    cnt += 1
    heap_set.add(num)

print(cnt)

