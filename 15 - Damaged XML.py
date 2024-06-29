import sys


def is_valid_xml(s):
    state = 1
    current_tag = ''
    stack = []
    for i in range(len(s)):
        symbol = s[i]
        if state == 1:
            if symbol == '<':
                state = 2
            else:
                return False

        elif state == 4:
            if symbol == '>':
                state = 1
            else:
                return False

        elif state == 2:
            if symbol == '/' or symbol.isalpha():
                current_tag += symbol
                state = 3
            else:
                return False

        elif state == 3:
            if symbol.isalpha():
                current_tag += symbol
            elif symbol == '>':
                if current_tag[0] == '/':
                    try:
                        if stack[-1] == current_tag[1:]:
                            stack.pop(-1)
                        else:
                            return False
                    except:
                        return False
                else:
                    stack.append(current_tag)

                current_tag = ''
                state = 1
            else:
                return False
    if stack:
        return False
    return True

s = input()

for i in range(len(s)):
    for symbol in '<>/abcdefghijklmnopqrstuvwxyz':
        if symbol == s[i]:
            continue
        candidate = s[:i] + symbol + s[i+1:]
        if is_valid_xml(candidate):
            print(candidate)
            sys.exit()