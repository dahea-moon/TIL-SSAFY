import sys
sys.stdin = open('5202.txt', 'r')

def select_sorting(data, i, n):
    min_num = i
    if i == n:
        return
    for j in range(i+1, n):
        if data[j][1] < data[min_num][1]:
            min_num = j
    data[i], data[min_num] = data[min_num], data[i]
    select_sorting(data, i+1, n)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    meetings = [list(map(int, input().split())) for _ in range(N)]
    possible = []

    select_sorting(meetings, 0, N)

    # possible.append(meetings[0])
    cnt = 1
    endt = meetings[0][1]
    for t in range(1, N):
        if meetings[t][0] >= endt and meetings[t] not in possible:
            # possible.append(meetings[t])
            endt = meetings[t][1]
            cnt += 1

    # print('#{} {}'.format(tc, len(possible)))
    print('#{} {}'.format(tc, cnt))




