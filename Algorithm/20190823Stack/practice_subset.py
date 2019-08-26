powerset = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

def ispromising(a, k, goal_sum, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, goal_sum):
    global maxcandidates
    c = [0] * maxcandidates

    if k == goal_sum:
        print(a)
    else:
        k += 1
        candi = ispromising(a, k, goal_sum, c)




maxcandidates = 2
nmax = 11
a = [0] * nmax
k = 0