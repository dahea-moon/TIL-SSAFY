import sys
sys.stdin = open('sudoku.txt', 'r')

def isright(sudoku):
    for r in range(9):
        visited = [0]*9
        for c in range(9):
            visited[sudoku[r][c]-1] = 1
        if 0 in visited:
            return 0

    for c in range(9):
        visited = [0]*9
        for r in range(9):
            visited[sudoku[r][c]-1] = 1
        if 0 in visited:
            return 0

    for r in range(0, 7, 3):
        visited = [0]*9
        for c in range(r, r+3):
            for i in range(3):
                visited[sudoku[r+i][c]-1] = 1
        if 0 in visited:
            return 0

    return 1

T = int(input())
for tc in range(1, T+1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(tc, isright(sudoku)))