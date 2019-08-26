import sys
sys.stdin = open('4874_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    cal = input().split()
    stack = []

    def calstack(s):
        n1 = stack.pop()
        n2 = stack.pop()
        if c == '+':
            stack.append(n1 + n2)
        elif c == '-':
            stack.append(n2 - n1)
        elif c == '*':
            stack.append(n1 * n2)
        elif c == '/':
            stack.append(int(n2 / n1))

    for c in cal:
        if c not in '*+/-.':
            stack.append(int(c))
        else:
            if c in '*+/-':
                if len(stack) >1:
                    calstack(c)
                else:
                    print('#{} {}'.format(tc, 'error'))
                    break
            elif c == '.':
                if len(stack) == 1:
                    print('#{} {}'.format(tc, stack[-1]))
                else:
                    print('#{} {}'.format(tc, 'error'))