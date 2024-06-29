from heapq import *

k, n = map(int, input().split())

heap = []
heapify(heap)
otv = []
places = [False] * k

for i in range(n):
    arr, dep = map(int, input().split())
    try:
        ans = heappop(heap)
        while ans[0] < arr:
            places[ans[1]] = False
            ans = heappop(heap)
        heappush(heap, ans)

    except IndexError:
        pass
    if len(heap) == k:
        print(0, i + 1)
        exit()
    new_place = -1
    for j in range(k):
        if not places[j]:
            new_place = j
            places[j] = True
            break
    x = [dep, new_place]
    heappush(heap, x)
    otv.append(new_place + 1)
print(*otv)

