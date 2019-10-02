def combination(j, k):
    global tr, m, nums, n

    if k == m:
        for t in tr:
            print(t, end=' ')
        print()
        return
    else:
        for i in range(j, n):
            if not visited[i]:
                visited[i] = 1
                tr.append(nums[i])
                combination(i, k+1)
                visited[i] = 0
                tr.pop()

n, m = 4, 2
nums = [x for x in range(1, n+1)]
tr = []
visited = [0]*n
combination(0, 0)

def comb(k, R):
    if k == R :
        result = []
        for kk in range(k):
            result.append(str(arr[kk]))
        print(' '.join(result))
    else:
        for i in range(k, n):
            arr[i], arr[k] = arr[k], arr[i]
            if k == 0:
                comb(k + 1, R)
            elif k > 0:
                if arr[k-1] < arr[k]:
                    comb(k+1, R)
            arr[i], arr[k] = arr[k], arr[i]

n, m = 4, 2
arr = [i for i in range(1, n+1)]
comb(0, m)

#3개 중 2개 선택 조합
N = 3
R = 2
a = [1,2,3]
t = [0]*2

def comb(n, r):
    if r == 0:
        print(t)
    elif n < r:
            return
    else:
        t[r-1] = a[n-1]
        comb(n-1, r-1)
        comb(n-1, r)

def comb(k, s):
    if k == R:
        print(t)
    else:
        for i in range(s, N-R+k):
            t[k] = a[i]
            comb(k+1, i+1)

#중복조합은 visited를 없앤다
def comb(n, r):
    if r == 0:
        print(t)
    elif n == 0:
        return
    else:
        t[r-1] = a[n-1]
        comb(n, r-1)
        comb(n-1, r)

comb(N, R)

def comb(k, s):
    if k == R:
        print(t)
    else:
        for i in range(s, N):
            t[k] = a[i]
            comb(k+1, i)

comb(0, 1)