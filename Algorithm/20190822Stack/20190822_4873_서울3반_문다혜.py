import sys
sys.stdin = open('4873.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    S = input()
    i = 0

    while i != len(S):
        if i+1 < len(S):
            if S[i] == S[i+1]:
                if i ==0:
                    S = S[2::]
                else:
                    S = S[0:i:] + S[i+2::]
                    i = 0
            else:
                i += 1
        else:
            break

    print(tc, len(S))