n = int(input())

for i in range(n):
    lst = list(map(float, input().split()))[1:]
    stack = [lst[0]]
    por = []
    for j in lst[1:]:
        if j > stack[-1]:
            for z in range(len(stack)):
                if j >= stack[-1]:
                    por.append(stack[-1])
                    stack.pop(-1)
            stack.append(j)
        elif j <= stack[-1]:
            stack.append(j)
    por += stack[::-1]
    for j in range(1, len(por)):
        if por[j - 1] > por[j]:
            print(0)
            break
    else:
        print(1)
