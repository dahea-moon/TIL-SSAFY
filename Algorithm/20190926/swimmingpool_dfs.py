import sys
sys.stdin = open('swimmingpool.txt', 'r')

def finding(i, chksum):
    global plans, minprice, prices

    if i > 11:
        if chksum < minprice:
            minprice = chksum
            return

    if plans[i] == 0:
        finding(i+1, chksum)

    if chksum + plans[i]*prices[0] < minprice:
        finding(i+1, chksum + plans[i]*prices[0])
    if chksum + prices[1] < minprice:
        finding(i+1, chksum + prices[1])
    if chksum + prices[2] < minprice:
        finding(i+3, chksum + prices[2])

T = int(input())
for tc in range(1, T+1):
    prices = list(map(int, input().split()))
    plans = list(map(int, input().split()))
    minprice = prices[-1]

    for i in range(12):
        if plans[i]:
            finding(i, 0)
            break

    print('#{} {}'.format(tc, minprice))
