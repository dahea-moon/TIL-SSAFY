import sys

sys.stdin = open('4861_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    rc, lp = map(int, input().split())
    words = [[i for i in input()] for m in range(rc)]
    pail = ''

    for r in range(row):
        if words[r] == words[r][::-1]:
            pail = ''.join(words[r])

    colo = [0]*row
    for c in range(col):
        for r in range(row):
            colo[r] = words[r][c]
            if colo == colo[::-1]:
                pail = ''.join(colo)

    print(pail, colo)
