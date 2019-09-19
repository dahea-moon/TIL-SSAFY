import sys
sys.stdin = open('bank.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    two = input()
    three = input()
    th_can = []

    for i in range(len(three)):
        if three[i] == '0':
            chk_1 = three[0:i] + '1' + three[i+1:]
            chk_2 = three[0:i] + '2' + three[i + 1:]
        elif three[i] == '1':
            chk_1 = three[0:i] + '0' + three[i+1:]
            chk_2 = three[0:i] + '2' + three[i + 1:]
        else:
            chk_1 = three[0:i] + '1' + three[i+1:]
            chk_2 = three[0:i] + '0' + three[i + 1:]
        th_can.append(chk_1)
        th_can.append(chk_2)

    for i in range(len(two)):
        if two[i] == '0':
            chk = two[0:i] + '1' + two[i+1:]
        else:
            chk = two[0:i] + '0' + two[i + 1:]

        result = 0
        for idx, val in enumerate(chk):
            if int(val):
                result += int(val) << (len(two)-1 - idx)

        result1 = result
        candi = []
        while result1 != 0:
            candi.append(result1%3)
            result1 //= 3

        candi_2 = ''
        while candi:
            candi_2 += str(candi.pop())

        if candi_2 in th_can:
            break

    print('#{} {}'.format(tc, result))