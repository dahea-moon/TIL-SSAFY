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

    sc_s = set()
    for i in range(1<<N):
        subset = 0
        for j in range(N+1):
            if i & (1<<j):
                subset += score[j]
        sc_s.add(subset)

    print('#{} {}'.format(tc, len(sc_s)))