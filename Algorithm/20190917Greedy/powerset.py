def powerset(arr, n):
    for i in range(0, (1<<n)):
        pset= []
        for j in range(n+1):
            if i & (1<<j):
                pset.append(arr[j])
        if sum(pset) == 0:
            print(pset)


def comb(n, r):
    global arr, tr

    if r == 0:
        if sum(tr) == 0:
            print(tr)
    elif n < r:
        return
    else:
        tr[r-1] = arr[n-1]
        comb(n-1, r-1)
        comb(n-1, r)


arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
n = len(arr)
powerset(arr, n)
tr = [0]*n
for i in range(0, n+1):
    comb(n, i)