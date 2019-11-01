import sys
sys.stdin = open('test.txt', 'r')

n, l = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(n)]
print(roads)
res = 0
for i in range(n):
    for j in range(n):


