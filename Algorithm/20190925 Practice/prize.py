import sys
sys.stdin = open('prize.txt', 'r')


def finding(i, j, n, cnt):
    global maxi
    if cnt == goal:
        ans = 0
        for e, d in enumerate(prize[::-1]):
            ans += d*(10**e)
        if maxi < ans:
            maxi = ans
        return
    if i == j == n-1:
        flag = True
        for s in prize:
            if prize.count(s) >= 2:
                flag = False
                break
        if flag:
            if (goal-cnt) % 2:
                prize[-1], prize[-2] = prize[-2], prize[-1]
                ans = 0
                for e, d in enumerate(prize[::-1]):
                    ans += d * (10 ** e)
                if maxi < ans:
                    maxi = ans
                return
            else:
                ans = 0
                for e, d in enumerate(prize[::-1]):
                    ans += d * (10 ** e)
                if maxi < ans:
                    maxi = ans
                return
        else:
            ans = 0
            for e, d in enumerate(prize[::-1]):
                ans += d * (10 ** e)
            if maxi < ans:
                maxi = ans
            return
    else:
        if prize[i] != chk[j]:
            for idx, v in enumerate(prize):
                if v == chk[j]:
                    prize[idx], prize[i] = prize[i], prize[idx]
                    finding(i + 1, j + 1, n, cnt + 1)
                    prize[idx], prize[i] = prize[i], prize[idx]
        else:
            finding(i + 1, j + 1, n, cnt)


T = int(input())
for tc in range(1, T+1):
    data = input().split()
    goal = int(data[1])
    prize = list((map(int, data[0])))
    chk = sorted(prize, reverse=True)

    cnt = 0
    i = j = 0
    n = len(prize)
    maxi = 0
    finding(i, j, n, cnt)
    print('#{} {}'.format(tc, maxi))

