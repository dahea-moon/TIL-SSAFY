def powerset(arr, k, input):
    global checked, sums

    if k == input:
        if sums == 10:
            print(subset)
            print(sums)
    else:
        if not checked[k]:
            checked[k] = 1
            sums += arr[k]
            subset.append(arr[k])
            powerset(arr, k+1, input)
            checked[k] = 0
            sums -= arr[k]
            subset.pop()
            powerset(arr, k + 1, input)

sets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sums = 0
subset = []
checked = [0]*10
powerset(sets, 0, 10)