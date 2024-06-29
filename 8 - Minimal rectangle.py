n = int(input())
min_x = 10 ** 10
max_x = - (10 ** 10)
min_y = 10 ** 10
max_y = - (10 ** 10)

for i in range(n):
    x, y = map(int, input().split())
    min_x = min(min_x, x)
    min_y = min(min_y, y)
    max_x = max(max_x, x)
    max_y = max(max_y, y)

print(min_x, min_y, max_x, max_y)
