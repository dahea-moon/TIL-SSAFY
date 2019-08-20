# 패턴찾기 알고리즘
pattern = 'is'
full = 'this is a book!'

#고지식한 패턴 알고리즘
def BruteForce(pattern, full):
    M = len(pattern)
    N = len(full)
    i = 0
    j = 0

    while j < M and i < N:
        if full[i] != pattern[j]:
            i = i - j
            j = -1
        j += 1
        i += 1
    if j == M:
        return i - M
    else:
        return -1

# KMP 알고리즘
def KMP(pattern, full):
    