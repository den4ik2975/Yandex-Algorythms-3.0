from queue import PriorityQueue
n = int(input())
lst = list(map(int, input().split()))
ans = 0
que = PriorityQueue()

for i in lst:
    que.put(i)
  
while que.qsize() > 1:
    summ = que.get() + que.get()
    ans += summ
    que.put(summ)

print("{:.2f}".format(round(ans * 5 / 100, 2)))