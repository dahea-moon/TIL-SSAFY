import sys
sys.stdin = open('honey.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    works = [list(map(int, input().split())) for _ in range(N)]
    incomes = [[0]*N for _ in range(N)]
    print(works)
    maxihoney = 0
    for r in range(N):
        for c in range(N-(M-1)):
            income = 0
            chk = 0
            for i in range(M):
                if c+i < N:
                    if chk + works[r][c+i] <= C:
                        chk += works[r][c+i]
                        income += works[r][c+i]**2
            for i in range(M):
                if c + i < N:
                    if works[r][c+i] >= chk:
                        if income < works[r][c + i] ** 2:
                            income = works[r][c + i] ** 2
            incomes[r][c] = income
            if maxihoney < income:
                maxihoney = income
                maxir, maxic = r, c
    print(incomes)
    for j in range(maxic, maxic+M):
        incomes[maxir][j] = 0
        incomes[maxir][j-M+1] = 0
    print(incomes)
    maxi2 = 0
    for a in incomes:
        if max(a) > maxi2:
            maxi2 = max(a)
    print(maxihoney, maxi2)
    print('#{} {}'.format(tc, maxihoney+maxi2))

