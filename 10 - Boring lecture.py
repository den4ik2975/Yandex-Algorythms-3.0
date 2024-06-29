s = input()
cnt = len(s)
otv = {}

for i in range(len(s)):
    if otv.get(s[i], -1) == -1:
        otv[s[i]] = 0
    otv[s[i]] += cnt * (i + 1)
    cnt -= 1

otv = dict(sorted(otv.items()))
for key, val in otv.items():
    print(f'{key}: {val}')