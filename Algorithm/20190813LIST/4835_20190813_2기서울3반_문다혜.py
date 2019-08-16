import sys
sys.stdin = open("4835.txt","r")

T = int(input())
for tc in range(1,T+1):
    N = list(map(int, input().split()))
    H = list(map(int, input().split()))
    count = N[1]
    data = []
    for i in range(0,N[0]-count+1):
        data.append(sum(H[i:i+count]))
    data = sorted(data)
    result = data[-1] - data[0]
    print("#{} {}".format(tc, result))