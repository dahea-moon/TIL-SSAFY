import sys
sys.stdin = open('5097_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))

    front = 0
    rear = N-1
    for m in range(M):
        nums.append(nums[front])
        front += 1
        rear += 1

    print('#{} {}'.format(tc, nums[front]))
