import sys
sys.stdin = open('testscore.txt', 'r')

def powerset(s):
    r = [[]]

    for e in s:
        temp = [x+[e] for x in r]
        r += temp

    return r

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    score = list(map(int, input().split()))

