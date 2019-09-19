import sys
sys.stdin = open('simple 2bite.txt', 'r')

pwd = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4,
       '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}

T = int(input())
for tc in range(1, T+1):
    R, C = map(int, input().split())
    data = [input() for _ in range(R)]

    for r in range(R):
        for c in range(C-1, -1, -1):
            if data[r][c] == '1':
                sr = r
                sc = c
                break

    code = [data[sr][sc-55:sc+1]]
    encode = [0]*8
    n = 0
    for i in range(0, 56, 7):
        raw = ''.join(code[0][i:i+7])
        encode[n] = pwd.get(raw)
        n += 1

    chk = 0
    for i in range(7):
        if i % 2:
            chk += encode[i]
        else:
            chk += encode[i]*3

    if (chk + encode[-1]) % 10 == 0:
        print('#{} {}'.format(tc, sum(encode)))
    else:
        print('#{} {}'.format(tc, 0))

