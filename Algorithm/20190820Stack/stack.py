value = input()
stack = []

def push(item, stack):
    stack.append(item)

def pop(stack):
    if len(stack) == 0:
        return False
    else:
        return stack.pop(-1)

