import sys
sys.stdin = open('5204.txt', 'r')

def merge(left, right):
    global cnt
    i = 0
    j = 0
    result = []

    if left[-1] > right[-1]:
        cnt += 1

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

def merge_sort(arr):
    global cnt

    if len(arr) <= 2:
        if len(arr) ==2:
            if arr[1] < arr[0]:
                arr[0], arr[1] = arr[1], arr[0]
                cnt += 1
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    cnt = 0
    res = merge_sort(nums)
    print(res)
    print('#{} {} {}'.format(tc, res[n//2], cnt))