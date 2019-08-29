import sys
sys.stdin = open('A2_sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mols = [list(map(int, input().split())) for _ in range(N)]
    delta = [0, 1, 2, 3]
    te = 0

    up = down = lt = rt = []
    for mol in mols:
        if mol[2] == 0:
            up.append((mol[0], mol[1], mol[3]))
        elif mol[2] == 1:
            down.append((mol[0], mol[1], mol[3]))
        elif mol[2] == 2:
            rt.append((mol[0], mol[1], mol[3]))
        elif mol[2] == 3:
            lt.append((mol[0], mol[1], mol[3]))

    bomb = set()
    for mu in up:
        for md in down:
            if mu[0] == md[0] and mu[1] < md[1]:
                bomb.add(mu)
                bomb.add(md)

        for mr in rt:
            if abs(mr[1])+abs(mu[1]) == abs(mu[0])-abs(mr[0]):
                bomb.add(mr)
                bomb.add(mu)

        for ml in lt:
            if abs(ml[1])-abs(mu[1]) == abs(ml[0])-abs(mu[0]):
                bomb.add(ml)
                bomb.add(mu)

    for md in down:
        for mr in rt:
            if abs(md[1])-abs(mr[1]) == abs(md[0])-abs(mr[0]):
                bomb.add(md)
                bomb.add(mr)

        for ml in lt:
            if abs(md[1])-abs(ml[1]) == abs(ml[0])-abs(md[0]):
                bomb.add(ml)
                bomb.add(md)

    for mr in rt:
        for ml in lt:
            if mr[1] == ml[1] and mr[0] < ml[0]:
                bomb.add(ml)
                bomb.add(mr)

    print(bomb)