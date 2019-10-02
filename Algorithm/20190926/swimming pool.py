import sys
sys.stdin = open('swimmingpool.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    prices = list(map(int, input().split()))
    plans = [0] + list(map(int, input().split()))
    months = []
    days = []
    for idx, plan in enumerate(plans):
        if plan:
            months += [idx]
            days += [plan]

    minprice = prices[-1]
    oneday = sum(days)*prices[0]
    if oneday < minprice:
        minprice = oneday

    onemonth = len(months)*prices[1]
    if onemonth < minprice:
        minprice = onemonth

    cases = []
    case_price = []
    for i in range(len(months)):
        mini = prices[1]
        price = 1
        if days[i]*prices[0] < mini:
            mini = days[i]*prices[0]
            price = 0
        cases += [months[i], prices[price]]
        case_price += [mini]

    if sum(case_price) < minprice:
        minprice = sum(case_price)

    isroll = []
    j = 0
    flag = True
    while flag:
        for i in range(j, len(months)-1):
            if i+1 != len(months)-1:
                if months[i+1]-months[i] != 1:
                    isroll += [months[j:i+1]]
                    j = i+1
                    break
            else:
                if months[i+1]-months[i] == 1:
                    isroll += [months[j:]]
                    j = i+1
                    break
        else:
            flag = False
    print(isroll)

    if len(isroll) > 1:
        chksum = 0
        for row in isroll:
            if len(row) > 2:
                tickets = len(row) // 3
                st = len(row) % 3
                for j in range(1, tickets + 1):
                    std = tickets * 3
                    for h in range(-1, len(case_price) - st - 2):
                        chk = case_price[: h + 1] + [prices[2] * j] + case_price[h + (3 * j + 1):]
                        chksum += sum(chk)
            else:

                if (tickets + 1) * prices[2] < minprice:
                    minprice = (tickets + 1) * prices[2]
    else:
        tickets = len(months) // 3
        st = len(months)%3
        for j in range(1, tickets+1):
            std = tickets*3
            for h in range(-1, len(case_price)-st-2):
                chk = case_price[: h+1] + [prices[2]*j] + case_price[h+(3*j+1):]
                if sum(chk) < minprice:
                    minprice = sum(chk)
        if (tickets+1)*prices[2]< minprice:
            minprice = (tickets+1)*prices[2]

    print('#{} {}'.format(tc, minprice))



