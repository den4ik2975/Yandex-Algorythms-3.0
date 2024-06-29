symbols = {}
cnt = 0

with open('input.txt', 'r') as f:
    txt = f.read()

for i in txt:
    if i != '\n' and i != ' ':
        num = ord(i)
        if symbols.get(num, 0) == 0:
            symbols[num] = 0
            cnt += 1
        symbols[num] += 1

symbols = dict(sorted(symbols.items()))
all_symbols = ''

maxx = 0
for key, val in symbols.items():
    all_symbols += str(chr(key))
    maxx = max(maxx, val)


ans = [all_symbols] + [' ' * cnt] * maxx

for i, val in enumerate(symbols.values()):
    for j in range(val, 0, -1):
        ans[j] = ans[j][:i] + '#' + ans[j][i + 1:]

for i in reversed(ans):
    print(i)


