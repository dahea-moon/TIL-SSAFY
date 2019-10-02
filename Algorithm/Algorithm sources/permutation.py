def perm_i():
    for i1 in range(1, 4):
        for i2 in range(1, 4):
            if i2 != i1:
                for i3 in range(1, 4):
                    if i3 != i1 and i3 != i2:
                        print(i1, i2, i3)


def construct_candidates(a, k, input, c):
    in_perm = [False] * N

    for i in range(k):
        in_perm[a[i]] = True

    ncandidates = 0
    for i in range(input):
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    return ncandidates


def perm_r_1(a, k, input):
    c = [0] * N

    if k == N:
        print(a[0] + 1, a[1] + 1, a[2] + 1)
    else:
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            perm_r_1(a, k + 1, input)


def perm_r_2(n, r):
    if r == 0:
        print(t[0], t[1], t[2])
    else:
        for i in range(n - 1, -1, -1):
            arr[i], arr[n - 1] = arr[n - 1], arr[i]
            t[r - 1] = arr[n - 1]
            perm_r_2(n - 1, r - 1)
            arr[i], arr[n - 1] = arr[n - 1], arr[i]


def perm_r_3(k):
    if k == R:
        print(arr[0], arr[1], arr[2])
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm_r_3(k + 1)
            arr[k], arr[i] = arr[i], arr[k]



def perm_r_4(k):
    if k == N:
        print(t[0], t[1], t[2])
    else:
        for i in range(N):
            if visited[i]: continue
            t[k] = arr[i]
            visited[i] = 1
            perm_r_4(k + 1)
            visited[i] = 0



print('순열 반복문')
perm_i()

N = 3
R = 3

print('순열 재귀문1')
a = [0] * N
perm_r_1(a, 0, 3)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


t = [0] * N
print('순열 재귀문2')
perm_r_2(N, R)


print('순열 재귀문3')
perm_r_3(0)


visited = [0] * N
print('순열 재귀문4')
perm_r_4(0)

#중복순열
def permutation(nums, n, k):
    global tr, m

    if k == m:
        for t in tr:
            print(t, end=' ')
        print()
    else:
        for i in range(n):
            tr.append(nums[i])
            permutation(nums, n, k+1)
            tr.pop()

print('내꺼')
n, m = 4, 2
nums = [x for x in range(1, n+1)]
tr = []
permutation(nums, n, 0)

def perm(k, R):
    if k == R :
        result = []
        for kk in range(k):
            result.append(str(t[kk]))
        print(' '.join(result))
    else:
        for i in range(n):
            t[k] = i + 1
            perm(k + 1, R)

n, m = 4, 2
t = [0] * m
perm(0, m)

def perm(n, r):
    if r == 0:
        print(t)
    else:
        for i in range(n-1, -1, -1):
            a[i], a[n-1] = a[n-1], a[i]
            t[r-1] = a[n-1]
            perm(n, r-1)
            a[i], a[n-1] = a[n-1], a[i]

def perm(k):
    if k == R:
        print(t)
    else:
        for i in range(0, N-1):
            t[k] = a[i]
            perm(k+1)

print('중복순열')
N = 4
R = 2
a = [1, 2, 3, 4]
t = [0]*2
perm(0)