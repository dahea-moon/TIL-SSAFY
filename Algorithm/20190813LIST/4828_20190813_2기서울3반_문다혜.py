import sys
sys.stdin = open("sample_input.txt", "r")

T=int(input())
for tc in range(1, T+1):
    C = int(input())
    N = list(map(int, input().split()))
    N = sorted(N)
    result = N[-1] - N[0]
    print("#{} {}".format(tc, result))