import sys
sys.stdin = open('palindrome2_input.txt', 'r')

T = 10
for tc in range(1, T+1):
    t = int(input())
    words = [[i for i in input()] for n in range(100)]

    max_num = 3
    r = 0
    while r < 100:
        for s in range(100):
            for c in range(max_num, 100):
                if words[r][s:s+c] == words[r][s:s+c][::-1]:
                    if max_num < len(words[r][s:s+c]):
                        max_num = len(words[r][s:s+c])
        r += 1

    cols = []
    for c in range(100):
        col = []
        for r in range(100):
            col.append(words[r][c])
        cols.append(col)

    r = 0
    while r < 100:
        for s in range(100):
            for c in range(max_num, 100):
                if cols[r][s:s + c] == cols[r][s:s + c][::-1]:
                    if max_num < len(cols[r][s:s + c]):
                        max_num = len(cols[r][s:s + c])
        r += 1

    print(max_num)