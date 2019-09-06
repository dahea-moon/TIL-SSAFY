from collections import deque

nums = deque()

for n in range(3):
    num = int(input())

    if len(nums) == 0:
        nums.append(num)
    elif len(nums) == 1:
        if nums[0] > num:
            nums.insert(0, num)
        else:
            nums.append(num)
    else:
        for i in range(len(nums)):
            idx = i
            for j in range(i - 1, -1, -1):
                if nums[j] > a[i]:
                    pos = j
            sd.insert(pos, a[i])

            nums.append(num)

print(nums)

