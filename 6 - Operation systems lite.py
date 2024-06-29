m = int(input())
n = int(input())
current_sys = []
for i in range(n):
    a, b = map(int, input().split())
    current_sys_copy = current_sys[:]
    for j in range(len(current_sys) - 1, -1, -1):
        n, m = current_sys_copy[j][0], current_sys_copy[j][1]
        if (a <= n <= b) or (a <= m <= b) or (n <= a <= m) or (n <= b <= m):
            del current_sys[j]
    current_sys.append((a, b))

print(len(current_sys))
