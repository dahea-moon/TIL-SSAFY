import sys
sys.stdin = open("input.txt", "r")

for tc in range(10):
    test_case = int(input())
    Numbers = [list(map(int, input().split())) for _ in range(100)]

    sum_l = []

    for x in range(len(Numbers)):
        r_sum = 0
        c_sum = 0
        tl_sum = 0
        tl_sum += Numbers[x][x]
        for y in range(len(Numbers)):
            r_sum += Numbers[x][y]
            c_sum += Numbers[y][x]
        sum_l.append(r_sum)
        sum_l.append(c_sum)
        sum_l.append(tl_sum)

    tr_sum = 0
    x, y = 0, 99
    for _ in range(len(Numbers)-1):
        tr_sum += Numbers[x][y]
        x += 1
        y -= 1
    sum_l.append(tr_sum)

    print(max(sum_l))
