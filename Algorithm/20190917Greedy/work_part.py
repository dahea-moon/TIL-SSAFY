import sys
sys.stdin = open('work_part.txt', 'r')

def sharework(arr, i, chk_prob):
    global checked, maxprob

    if i == N:
        maxprob = chk_prob
    else:
        for t in range(N):
            if not checked[t]:
                if maxprob < chk_prob*arr[i][t]/100:
                    checked[t] = 1
                    sharework(arr, i+1, chk_prob*arr[i][t]/100)
                    checked[t] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    workprob = [list(map(int, input().split())) for _ in range(N)]

    checked=[0]*N
    maxprob = 0
    sharework(workprob, 0, 1)
    print('#%d %0.6f' % (tc, maxprob*100))