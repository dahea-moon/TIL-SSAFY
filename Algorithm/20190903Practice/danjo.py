import sys
sys.stdin = open('danjo_input.txt', 'r')

def isdanjo(ns):
    for i in range(len(ns)-1):
        if int(ns[i]) > int(ns[i+1]):
            return False
    return True

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    maxnum = -1
    for m in range(N-1):
        for n in range(m+1, N):
            n1 = nums[m]
            n2 = nums[n]
            if isdanjo(str(n1*n2)):
                if n1*n2 > maxnum:
                    maxnum = n1*n2

    print('#{} {}'.format(tc, maxnum))