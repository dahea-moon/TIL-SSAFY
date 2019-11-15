ppl = [0, 1, 2, 3, 4, 5]

def powerset(k, n):
    if k == n:
        print(comb)
    else:
        for z in range(2):
            comb[k] = z
            powerset(k+1, n)

comb = [0]*6
powerset(0, 6)