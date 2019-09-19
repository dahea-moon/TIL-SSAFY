import sys
sys.stdin = open('5185.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    data = input().split()

    output = ''
    for tbit in data[1]:
        try:
            t = int(tbit)
        except ValueError:
            t = ord(tbit) - ord('A') + 10

        for j in range(3, -1, -1):
            output += '1' if t & (1 << j) else '0'

    print('#{} {}'.format(tc, output))