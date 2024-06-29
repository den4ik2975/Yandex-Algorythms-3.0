from collections import deque
n = int(input())
fr = deque()
sc = deque()
ln_fr = 0
ln_sc = 0

for i in range(n):
    goblin = input()
    if goblin[0] == '-':
        print(''.join(fr.popleft()))
        ln_fr -= 1
    elif goblin[0] == '+':
        sc.append(goblin[2:])
        ln_sc += 1
    else:
        if (ln_sc + ln_fr) % 2 == 1:
            sc.appendleft([goblin[2:]])
            ln_sc += 1
        else:
            fr.append([goblin[2:]])
            ln_fr += 1
    if ln_sc - ln_fr >= 1:
        fr.append([''.join(sc.popleft())])
        ln_fr += 1
        ln_sc -= 1
