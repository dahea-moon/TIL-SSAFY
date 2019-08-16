import sys
sys.stdin = open("metalstick_input.txt", "r")

T = int(input())
for tc in range(1,T+1):
    nm = int(input())
    raw = list(map(int,input().split()))
    mss = [0]*nm

    for i in range(nm):
        mss[i] = (raw[2*i], raw[2*i+1])
    
    for k in range(nm):
        count = 0
        for i in range(nm):
            if mss[k][0] == mss[i][1]:
                count += 1
        if count == 0:
            mss[k], mss[0] = mss[0], mss[k]

    # for k in range(nm):
    #     count = 0
    #     for i in range(nm):
    #         if mss[k][1] == mss[i][0]:
    #             count += 1
    #     if count == 0:
    #         mss[-1], mss[k] = mss[k], mss[-1]

    for i in range(1, nm-1):
        for h in range(1, nm-1):
            if mss[i][1] == mss[h][0]:
                mss[i+1], mss[h] = mss[h], mss[i+1]

    print(mss)