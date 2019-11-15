import sys
sys.stdin = open('test.txt', 'r')

def turning(magnet, dir):
    new = [0] * 8
    if dir == 1:
        for j in range(8):
            if j == 7:
                new[0] = magnet[j]
            else:
                new[j+1] = magnet[j]
    else:
        for j in range(8):
            if j == 0:
                new[7] = magnet[j]
            else:
                new[j-1] = magnet[j]
    return new

def solve(n, dir):
    global magnets
    new_magnets = magnets[:]
    if n == 1:
        o_r = magnets[n-1][2]
        new_magnets[n-1] = turning(magnets[n-1], dir)
        for p in range(1, 4):
            n_r, n_l = magnets[n - 1 + p][2], magnets[n - 1 + p][6]
            if o_r != n_l:
                dir = -dir
                new_magnets[n - 1 + p] = turning(magnets[n - 1 + p], dir)
            else:
                break
            o_r, o_l = n_r, n_l
    elif n == 4:
        o_l = magnets[n-1][6]
        new_magnets[n-1] = turning(magnets[n-1], dir)
        for p in range(1, 4):
            n_r, n_l = magnets[n - 1 - p][2], magnets[n - 1 - p][6]
            if o_l != n_r:
                dir = -dir
                new_magnets[n - 1 - p] = turning(magnets[n - 1 - p], dir)
            else:
                break
            o_r, o_l = n_r, n_l
    elif n == 2:
        o_r, o_l = magnets[n-1][2], magnets[n-1][6]
        new_magnets[n-1] = turning(magnets[n-1], dir)

        n_r, n_l = magnets[0][2], magnets[0][6]
        if o_l != n_r:
            new_magnets[0] = turning(magnets[0], -dir)

        n_r, n_l = magnets[2][2], magnets[2][6]
        if o_r != n_l:
            new_magnets[2] = turning(magnets[2], -dir)
            o_r, o_l = n_r, n_l
            n_r, n_l = magnets[3][2], magnets[3][6]
            if o_r != n_l:
                new_magnets[3] = turning(magnets[3], dir)

    else:
        o_r, o_l = magnets[n-1][2], magnets[n-1][6]
        new_magnets[n-1] = turning(magnets[n-1], dir)

        n_r, n_l = magnets[3][2], magnets[3][6]
        if o_r != n_l:
            new_magnets[3] = turning(magnets[3], -dir)

        n_r, n_l = magnets[1][2], magnets[1][6]
        if o_l != n_r:
            new_magnets[1] = turning(magnets[1], -dir)
            o_r, o_l = n_r, n_l
            n_r, n_l = magnets[0][2], magnets[0][6]
            if o_l != n_r:
                new_magnets[0] = turning(magnets[0], dir)

    return new_magnets


t = int(input())
for tc in range(1, t+1):

    k = int(input())
    magnets = [list(map(int, input().split())) for _ in range(4)]
    turns = [tuple(map(int, input().split())) for _ in range(k)]

    for i in range(k):
        n, dir = turns[i]
        magnets = solve(n, dir)

    res = 0
    for r in range(4):
        if magnets[r][0] == 1:
            if r == 0:
                res += 1
            elif r == 1:
                res += 2
            elif r == 2:
                res += 4
            elif r == 3:
                res += 8

    print('#{} {}'.format(tc, res))



