import sys
sys.stdin = open('palindrome1_input.txt', 'r')

T=10
for tc in range(1,T+1):
    lp = int(input())
    words = [[i for i in input()] for m in range(8)]
    cnt = 0

    for r in range(8):
        for c in range(8-lp+1):
            pl = [0]*lp
            if words[r][c] == words[r][c+lp-1]:
                for p in range(lp):
                    pl[p] = words[r][c+p]
                    if pl == pl[::-1]:
                        cnt += 1

    for c in range(8):
        for r in range(8-lp+1):
            pl = [0]*lp
            if words[r][c] == words[r+lp-1][c]:
                for p in range(lp):
                    pl[p] = words[r+p][c]
                    if pl == pl[::-1]:
                        cnt += 1

    print(cnt)