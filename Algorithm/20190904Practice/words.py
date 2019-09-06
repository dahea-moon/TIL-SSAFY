import sys
sys.stdin = open('words.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    board = [input().split() for _ in range(N)]

    cnt = 0
    for r in range(N):
        chk = 0
        for c in range(N):
            if board[r][c] == '1':
                chk += 1
                if chk == K and c == N-1:
                    cnt += 1
                if chk == K and c+1 < N and board[r][c+1] == '0':
                    cnt += 1
            elif board[r][c] =='0':
                chk = 0

    for c in range(N):
        chk = 0
        for r in range(N):
            if board[r][c] == '1':
                chk += 1
                if chk == K and r == N-1:
                    cnt += 1
                if chk == K and r+1 < N and board[r+1][c] == '0':
                    cnt += 1
            elif board[r][c] == '0':
                chk = 0

    print(cnt)