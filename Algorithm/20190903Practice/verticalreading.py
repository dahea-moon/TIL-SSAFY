import sys
sys.stdin = open('vertical_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    board = [list(input()) for _ in range(5)]

    result = ''
    for c in range(15):
        for r in range(5):
            try:
                result += board[r][c]
            except IndexError:
                pass

    print('#{} {}'.format(tc, result))