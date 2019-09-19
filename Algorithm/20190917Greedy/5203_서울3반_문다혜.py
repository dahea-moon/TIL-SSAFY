import sys
sys.stdin = open('5203.txt', 'r')

def comb(arr, n, r, tr, i):
    global cards, res

    if r == 0:
        tr += [cards[i]]
        if isrun(tr) or istriplet(tr):
            res = 1
        tr.pop()
    elif n < r:
        return
    else:
        tr[r-1] = arr[n-1]
        comb(arr, n-1, r-1, tr, i)
        comb(arr, n-1, r, tr, i)


def istriplet(arr):
    if arr[0] == arr[1] == arr[2]:
        return True
    else:
        return False

def isrun(arr):
    cnt = 0
    test = sorted(arr)
    if test[2] - test[1] == 1:
        cnt += 1
    if test[1] - test[0] == 1:
        cnt += 1
    if cnt == 2:
        return True
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    p1 = []
    p2 = []

    res = 0
    for i in range(12):
        if i % 2:
            if len(p2) == 2:
                tmp = p2 + [cards[i]]
                if istriplet(tmp) or isrun(tmp):
                    res = 2
                    break
            if len(p2) > 2:
                comb(p2, len(p2), 2, [0, 0], i)
                if res == 1:
                    res = 2
                    break
            p2.append(cards[i])
        else:
            if len(p1) == 2:
                tmp = p1 + [cards[i]]
                if istriplet(tmp) or isrun(tmp):
                    res = 1
                    break
            if len(p1) > 2:
                comb(p1, len(p1), 2, [0, 0], i)
                if res == 1:
                    break
            p1.append(cards[i])

    print('#{} {}'.format(tc, res))

