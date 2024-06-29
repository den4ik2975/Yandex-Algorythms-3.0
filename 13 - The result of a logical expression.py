s = input()

priority = {
    '!': 3,
    '&': 2,
    '|': 1,
    '^': 1,
    '(': -999
}

polska = []
stack = []
for i in s:
    if i == '1' or i == '0':
        polska.append(i)
    elif i == '(':
        stack.append('(')
    elif i == ')':
        for j in stack[::-1]:
            if j == '(':
                stack.pop(-1)
                break
            polska.append(j)
            stack.pop(-1)
    else:
        for j in stack[::-1]:
            if priority[stack[-1]] >= priority[i]:
                polska.append(stack[-1])
                stack.pop(-1)
        stack.append(i)

polska += stack[::-1]
stack.clear()

for i in polska:
    if i == '1' or i == '0':
        stack.append(int(i))
    elif i == '&':
        stack = stack[:-2] + [int(stack[-1] * stack[-2])]
    elif i == '^':
        stack = stack[:-2] + [int(stack[-1] ^ stack[-2])]
    elif i == '|':
        stack = stack[:-2] + [int(stack[-1] | stack[-2])]
    elif i == '!':
        stack[-1] = int(not stack[-1])

print(stack[0])
