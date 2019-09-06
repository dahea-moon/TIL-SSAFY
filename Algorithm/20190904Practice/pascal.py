import sys
sys.stdin = open('pascal.txt', 'r')

T = int(input())
for tc in range(T):
    n = int(input())
    print('#{}' .format(tc+1))
    for i in range(n):
        p = 1
        plist = [p]
        print('1', end= ' ')
        for j in range(i):
            p = p * (i-j) / (j + 1)
            plist.append(int(p))
            print(str(int(p)), end=' ')
        print()