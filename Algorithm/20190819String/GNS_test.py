import sys
sys.stdin = open('GNS_test_input.txt', 'r')

T = int(input())
for _ in range(1, T+1):
    C = input().split()
    N = input().split()
    tc = C[0]

    numbers = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    raw = []
    result = ''

    for num in N:
        raw.append(numbers[num])

    raw.sort()

    for num in raw:
        for key, val in numbers.items():
            if num == val:
                result += ' ' + str(key)

    print("{} {}".format(tc, result))
