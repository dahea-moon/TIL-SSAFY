import sys
sys.stdin = open("subset_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    case = list(map(int,input().split()))
    num_value = case[0]
    for_sum = case[1]
    numbers = [0]*12
    count = 0

    idx = 0
    for i in range(1, 13):
        numbers[idx] = i
        idx += 1
    
    for n in range(1, 1<<12):
        subset = []
        for i in range(13):
            if n & (1<<i):
                subset.append(numbers[i])
        if len(subset) == num_value:     
            subset_sum = sum(subset)
            if subset_sum == for_sum:
                count += 1

    print("#{} {}".format(tc, count)) 
