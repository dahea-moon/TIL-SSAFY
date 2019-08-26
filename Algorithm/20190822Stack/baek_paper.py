import sys
sys.stdin = open('paper.txt', 'r')

N = int(input())
full = [[0]*101 for r in range(101)]

def paper(n, f):
    cnt = 0
    for r in range(101):
        for c in range(101):
            if f[r][c] == n:
                cnt += 1
    return cnt

for n in range(1,N+1):
    R, C, W, H = map(int, input().split())
    if 0 <= R+H <= 100 and 0<= C+W <=100:
        for r in range(R, R+H):
            for c in range(C, C+W):
                full[r][c] = n

for n in range(1, N+1):
    print(paper(n,full))

# for n in range(1, N+1):
#     cnt = 0
#     for r in range(101):
#         for c in range(101):
#             if full[r][c] == n:
#                 cnt += 1
#     print(cnt)

