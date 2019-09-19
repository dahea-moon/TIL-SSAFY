def bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += '1' if i & (1<<j) else '0'
    print(output)

for i in range(-7,6):
    print('%3d = ' % i, end='')
    bbit_print(i)
