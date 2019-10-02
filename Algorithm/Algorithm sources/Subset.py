"""
비트 연산자
& == 비트 단위로 AND 연산
| == 비트 단위로 OR 연산
<< num == 피연산자의 비트 열을 왼쪽으로 num 만큼 이동
>> num == 피연산자의 비트 열을 오른쪽으로 num 만큼 이동
<< 연산자는 2^num 만큼 비트 값이 변한ㄷ. << 은 곱하기 2^num, >> 은 나누기 2^num
"""

arr = [1, 2, 3, 4, 5]
n = len(arr) # 원소의 개수

for i in range(1<<n): # 1<<n == 부분 집합의 개수
    for j in range(n+1): # 원소의 수만큼 비트를 비교
        if i & (i<<j): # and 연산 후 i의 j 번째 비트가 1, 즉 True 이면 j번째 원소 출력
            print(arr[j])

def powersetlist(s):
    r = [[]]
    for e in s:
        temp = [x+[e] for x in r]
        r += temp
    print(r)

def power_set_i():
    bit = [0, 0, 0]
    for i in range(2):
        bit[0] = i
        for j in range(2):
            bit[1] = j
            for k in range(2):
                bit[2] = k
                print(bit)

def power_set_r(k):
    if k == N:
        print(a)
    else:
        a[k] = 1
        power_set_r(k + 1)
        a[k] = 0
        power_set_r(k + 1)

print('부분집합 반복문')
power_set_i()

N = 3
a = [0] * N
print('부분집합 재귀문')
power_set_r(0)