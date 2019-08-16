import sys
sys.stdin = open("4834_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
	N = int(input())
	C = list(map(int, input().split()))
    check = set(C)
    data = {}
    keys = []
    values = []
    for i in check:
        data[i] = C.count(i)
    for key, value in data.items():
        keys.append(key)
        values.append(value)
result = max(values)
number = keys[values.index(result)]
print('#{} {} {}'.format(tc, number, result))
