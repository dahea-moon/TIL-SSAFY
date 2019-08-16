import sys
sys.stdin = open("metalstick_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    nm = int(input())
    raw = list(map(int,input().split()))
    mss = [0]*nm
    result = []

    for i in range(nm):
        mss[i] = (raw[2*i], raw[2*i+1])
    
    for k in range(nm):
        count = 0
        for i in range(nm):
            if mss[k][0] == mss[i][1]:
                count += 1
        if count == 0:
            result.append(mss[k])
    
    while len(mss) > len(result):
        for i in range(nm):
            if mss[i][0] == result[-1][1]:
                result.append(mss[i])
    
    final_string = ''
    for i in result:
        for j in range(2):
            final_string += ' ' + str(i[j])
    
    print("#{} {}".format(tc, final_string))