from collections import deque

n, k = map(int, input().split())
seq = list(map(int, input().split()))

window = deque()
for i in range(k):
    while window and seq[i] < seq[window[-1]]:
        window.pop()
    window.append(i)

for i in range(k, n):
    print(seq[window[0]])

    while window and window[0] <= i - k:
        window.popleft()

    while window and seq[i] < seq[window[-1]]:
        window.pop()
    window.append(i)

print(seq[window[0]])
