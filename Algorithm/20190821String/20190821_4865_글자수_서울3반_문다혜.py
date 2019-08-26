import sys
sys.stdin = open('4865_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    s1 = input()
    s2 = input()
    check = {}

    for char in s1:
        check[char] = s2.count(char)

    cnt = []
    for num in check.values():
        cnt.append(num)

    print('#{} {}'.format(tc, max(cnt)))