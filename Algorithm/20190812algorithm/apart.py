import sys
import time
sys.stdin = open("input.txt", "r")

T = 10
stime = time.time()
for tc in range(1, T+1):
    N = int(input())
    H = list(map(int,input().split()))
    count = 0
    for i in range(2, N-2):
        check = [H[i-2], H[i-1], H[i], H[i+1], H[i+2]]
        if H[i] == max(check):
            max_floor = H[i]
            check.pop(check.index(max_floor))
            second_max = max(check)
            count += max_floor - second_max
    print("#{} {}".format(tc, count))
etime = time.time() - stime
print(etime)
