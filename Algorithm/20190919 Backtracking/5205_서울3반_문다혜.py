import sys
sys.stdin = open('5205.txt', 'r')

def quicksort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quicksort(arr, l, s-1)
        quicksort(arr, s+1, r)

def partition(arr, p, r):
    x = arr[r]
    i = p
    for j in range(p, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    nums = list(map(int, input().split()))

    quicksort(nums, 0, len(nums) - 1)

    print('#{} {}'.format(tc, nums[n//2]))