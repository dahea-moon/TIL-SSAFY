import sys
sys.stdin = open("specialsort_input.txt", "r")

T = int(input())

def isOdd(number):
    if number % 2:
        return True
    else:
        return False

for tc in range(1, T+1):
    N = int(input())
    V = list(map(int,input().split()))

    for i in range(N):
        if isOdd(i) == False:
            maxnum = V[i]
            for n in range(N-i):
                if maxnum < V[i+n]:
                    maxnum = V[i+n]
                    V[i], V[i+n] = V[i+n], V[i]

        if isOdd(i) == True:
            minnum = V[i]
            for n in range(N-i):
                if minnum > V[i+n]:
                    minnum = V[i+n]
                    V[i], V[i+n] = V[i+n], V[i]
    
    V = ' '.join(map(str, V[:10]))
    print("#{} {}".format(tc, V))
