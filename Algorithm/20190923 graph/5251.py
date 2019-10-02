import sys
sys.stdin = open('5251.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    links = [list(map(int, input().split())) for _ in range(E)]
