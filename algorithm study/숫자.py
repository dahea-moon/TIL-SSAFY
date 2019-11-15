import sys
sys.stdin = open('test.txt', 'r')

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    signs = list(map(int, input().split()))
    nums = list(map(int, input().split()))
