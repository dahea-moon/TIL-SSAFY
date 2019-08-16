arr = [1, 5, -9, 6, -2, 3, -5, 4, 9, 7]

for i in range(1, 1 << len(arr)):
    subset = []

    for j in range(len(arr)):
        if i & (1 << j):
            subset.append(arr[j])
            sub_sum = 0
            for h in subset:
                sub_sum += h
            if sub_sum == 0:
                print(subset)
