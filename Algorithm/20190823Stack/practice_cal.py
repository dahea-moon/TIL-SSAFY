cal = [2,'+',3,'*',4,'/',5]
stack = []
result = []

for i in cal:
    if isinstance(i,int):
        result.append(i)
    else:
        if i in '+-':
            if stack[-1] in '+-':
                result.append(stack[-1])
                stack.append(i)
            elif stack[-1] in '*/':
                stack.pop()
        elif i in '*/':
            if stack[-1] in '+-':
                result.append(stack[-1])
                stack.pop()
            elif stack[-1] in '*/':
                stack.append(i)

print(result)
