import sys
sys.stdin = open('5207.txt', 'r')

def binary(arr, low, high, key):
    global way, cnt

    mid = (low+high) // 2
    if key == arr[mid]:
        cnt += 1
        return
    elif key < arr[mid]:
        if way == 0:
            return
        way = 0
        return binary(arr, low, mid-1, key)
    else:
        if way == 1:
            return
        way = 1
        return binary(arr, mid+1, high, key)

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))

    cnt = 0
    for i in b:
        if i in a:
            way = 2
            binary(a, 0, n-1, i)

    print('#{} {}'.format(tc, cnt))

