origin = [2, 4, 5, 6, 7, 4, 1, 3, 4, 2, 5, 6, 4, 6, 7, 8, 4, 5] # 1~8 --> max_value == 8
sorted_origin = [0]*len(origin)
counting = [0]*9  # max_value + 1

# 각 원소의 개수 세기
for i in range(len(origin)):
    counting[origin[i]] += 1

# 각 원소가 들어갈 index 위치와 갯수 표기
for i in range(1, len(counting)):
    counting[i] += counting[i-1]

# 거꾸로 순환하면서 정렬될 리스트에 원소 삽입
for j in range(len(origin)-1, -1, -1):
    sorted_origin[counting[origin[j]]-1] = origin[j]
    counting[origin[j]] -= 1

print(sorted_origin)