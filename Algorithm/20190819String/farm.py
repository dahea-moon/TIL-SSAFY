import sys
sys.stdin = open('farm.txt', 'r')

num = int(input())
datas = []
data = []
for _ in range(6):
    com = list(map(int, input().split()))
    datas.append(com[0])
    data.append(com[1])

full = [0]*2
j = 0
for i in range(len(datas)):
    if datas.count(datas[i]) == 1:
        full[j] = data[i]
        j += 1

data = data + data


for i in range(1, len(data)-1):
    if (data[i-1] + data[i+1]) == full[0]:
        nl = data[i]
    if (data[i - 1] + data[i + 1]) == full[1]:
        nr = data[i]

al = full[0]*full[1]
no = nl*nr
result = num * (al- no)
print(result)