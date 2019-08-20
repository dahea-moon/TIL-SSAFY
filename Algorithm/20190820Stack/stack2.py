def isRight(string):
    check = []
    for i in range(len(string)):
        if string[i] == '(':
            check.append(string[i])

    if len(check) == 0:
        return False

    for i in range(len(string)):
        if string[i] == ')':
            check.pop(-1)

    if len(check) == 0:
        return True
    else:
        return False


print(isRight('((()((((()()((()())((())))))'))