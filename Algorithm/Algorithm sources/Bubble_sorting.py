# 인접한 두 개의 원소를 비교하며 자리를 계속 교환
# 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬
# 시간 복잡도: O(n^2)

origin = [2, 5, 9, 4, 1, 7, 8, 10, 3, 6]
n = len(origin)

for i in range(n):
    for j in range(0, n-i-1):
        if origin[j] > origin[j+1]:
            origin[j], origin[j+1] = origin[j+1], origin[j]

print(origin)
