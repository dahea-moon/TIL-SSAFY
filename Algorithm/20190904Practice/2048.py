import sys
sys.stdin = open('2048.txt', 'r')

def game(str, board, n):
    if str == 'right':
        for r in range(n):
            for c in range(n-1, -1, -1):
                if board[r][c] == 0:
                    continue
                for i in range(c-1,-1,-1):
                    if board[r][i] != 0 and (board[r][i] > board[r][c] or board[r][i] < board[r][c]):
                        break
                    elif board[r][i] == board[r][c]:
                        board[r][c] += board[r][c]
                        board[r][i] = 0
                        break
        for r in range(n):
            for c in range(n-1, -1, -1):
                if board[r][c] == 0:
                    for i in range(c-1,-1,-1):
                        if board[r][i] != 0:
                            board[r][c] = board[r][i]
                            board[r][i] = 0
                            break
    elif str == 'left':
        for r in range(n):
            for c in range(n):
                if board[r][c] == 0:
                    continue
                for i in range(c+1, n):
                    if board[r][i] != 0 and (board[r][i] > board[r][c] or board[r][i] < board[r][c]):
                        break
                    elif board[r][i] == board[r][c]:
                        board[r][c] += board[r][c]
                        board[r][i] = 0
                        break
        for r in range(n):
            for c in range(n):
                if board[r][c] == 0:
                    for i in range(c+1,n):
                        if board[r][i] != 0:
                            board[r][c] = board[r][i]
                            board[r][i] = 0
                            break
    elif str == 'up':
        for c in range(n):
            for r in range(n):
                if board[r][c] == 0:
                    continue
                for i in range(r+1, n):
                    if board[i][c] != 0 and (board[i][c] > board[r][c] or board[i][c] < board[r][c]):
                        break
                    elif board[i][c] == board[r][c]:
                        board[r][c] += board[r][c]
                        board[i][c] = 0
                        break
        for c in range(n):
            for r in range(n):
                if board[r][c] == 0:
                    for i in range(r+1, n):
                        if board[i][c] != 0:
                            board[r][c] = board[i][c]
                            board[i][c] = 0
                            break
    elif str == 'down':
        for c in range(n):
            for r in range(n-1, -1, -1):
                if board[r][c] == 0:
                    continue
                for i in range(r-1, -1, -1):
                    if board[i][c] != 0 and (board[i][c] > board[r][c] or board[i][c] < board[r][c]):
                        break
                    elif board[i][c] == board[r][c]:
                        board[r][c] += board[r][c]
                        board[i][c] = 0
                        break
        for c in range(n):
            for r in range(n-1, -1, -1):
                if board[r][c] == 0:
                    for i in range(r-1, -1, -1):
                        if board[i][c] != 0:
                            board[r][c] = board[i][c]
                            board[i][c] = 0
                            break

    return board


T = int(input())
for tc in range(1, T+1):
    raw = input().split()
    n = int(raw[0])
    str = raw[1]
    board = [list(map(int, input().split())) for _ in range(n)]
    print('#{}'.format(tc))
    result = game(str,board,n)
    for r in range(n):
        for c in range(n):
            print(board[r][c], end=' ')
        print()
