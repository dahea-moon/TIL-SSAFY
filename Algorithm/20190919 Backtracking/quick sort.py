# data = [11, 45, 23, 81, 28, 34, 99, 22, 17, 8]
data = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

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

quicksort(data, 0, len(data)-1)

print(data)

def partitionh(arr, l, r):
    p = l
    i = l
    j = r
    while i < j:
        while i < r and arr[i] <= arr[p]:
            i += 1
        while j > l and arr[j] >= arr[p]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[p], arr[j] = arr[j], arr[p]

    return j