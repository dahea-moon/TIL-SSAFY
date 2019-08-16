def Counting_Sort(a, b, k):
    c = [0] * k
    for i in range(0, len(b)):
        c[a[i]] += 1
    for i in range(1, len(c)):
        c[i] += c[i-1]
    for i in range(len(b)-1, -1, -1):
        b[c[a[i]]-1] = a[i]
        c[a[i]] -= 1
    return b

print(Counting_Sort([0,4,1,3,1,2,4,1],[0]*8,5))