import sys
sys.stdin = open("colors_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    array = [list(map(int,input().split())) for _ in range(N)]
    matrix = [[0]*10 for _ in range(10)]

    for i in range(len(array)):
        color = array[i][-1]
        r1, c1 = array[i][0], array[i][1]
        r2, c2 = array[i][2], array[i][3]
        
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                matrix[r][c] += color
    
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 3:
                count += 1
    
    print("#{} {}".format(tc, count))
