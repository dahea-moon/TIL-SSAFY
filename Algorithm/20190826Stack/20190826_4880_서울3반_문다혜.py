import sys
sys.stdin = open('4880_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    rsp = list(map(int, input().split()))

    def winner(g):
        if g[0]==1:
            if g[1]==1 or g[1]==3:
                return g[0]
            elif g[1]==2:
                return g[1]
        if g[0]==2:
            if g[1]==2 or g[1]==1:
                return g[0]
            elif g[1]==3:
                return g[1]
        if g[0]==3:
            if g[1]==3 or g[1]==2:
                return g[0]
            elif g[1]==1:
                return g[1]


    def div(a,b):
        if a == b:
            return a
        else:
            rsp1 = div(a,(a+b)//2)
            rsp2 = div((a+b)//2 +1,b)

        return winner(rsp1), winner(rsp2)

    a = 1
    b = N
    print(div(a,b))
