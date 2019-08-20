T = int(input())

def isRight(s):
    stack = []

    if s[0] == '}' or s[0] == ')':
        return 0

    for i in s:
        if i in '{(':
            stack.append(i)
        elif i in '})':
            if len(stack) == 0:
                return 0
            elif i == ')' and stack[-1] != '(' or i =='}' and stack[-1] != '{':
                return 0
            else:
                stack.pop()

    if len(stack) == 0:
        return 1
    else:
        return 0

for tc in range(1, T + 1):
    s = str(input())
    print('#{} {}'.format(tc, isRight(s)))
