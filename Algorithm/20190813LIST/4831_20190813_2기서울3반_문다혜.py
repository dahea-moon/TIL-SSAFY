import sys
sys.stdin = open("4831_input.txt", "r")

T=int(input())
for tc in range(1, T+1):
    D = list(map(int,input().split()))
    Charger_Busstops = list(map(int,input().split()))
    Going_Once= D[0]
    Num_of_Busstops = D[1]
    Num_of_Charger = D[2]
    count = 0
    i = 0
    distance = []

    for idx in range(len(Charger_Busstops)-1):
        distance.append(Charger_Busstops[idx+1]-Charger_Busstops[idx])
    distance.append(Num_of_Busstops-Charger_Busstops[-1])
    distance.append(Charger_Busstops[0])

    if max(distance) > Going_Once:
        count = 0
    else:
        while i + Going_Once < Num_of_Busstops :
            if i + Going_Once in Charger_Busstops:
                count += 1
                i = i + Going_Once
            else:
                i -= 1

    print("#{} {}".format(tc, count))

