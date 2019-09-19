# 5 x 5 2_dimensional array
two_d = [[0 for _ in range(5)] for _ in range(5)]

# 2디 리스트 행 우선으로 돌기
for i in range(len(two_d)):
    for j in range(len(two_d[i])):
        two_d[i][j]

# 2디 리스트 열 우선으로 돌기
for i in range(len(two_d[0])):
    for j in range(len(two_d)):
        two_d[j][i]

# 2디 리스트 지그재그 순회 (0행 앞부터, 1행 뒤부터, 2행 앞부터, ...)
for i in range(len(two_d)):
    for j in range(len(two_d[i])):
        two_d[i][j+(j-1-2*j)*(i%2)]
        # 앞부터 보는 짝수행은 0을 곱하여, j를 정렬순으로 돌게함
        # 뒤부터 보는 홀수행은 1을 곱하여, j를 역정렬순으로 돌게함

# 델타를 이용한 2차 배열 탐색
dx = [-1, 1, 0, 0] # 상하좌우 순으로 탐색
dy = [0, 0, -1, 1]

for x in range(len(two_d)):
    for y in range(len(two_d[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dx[i]

# 전치행렬 --> 대각선을 기준으로 2차 배열 뒤집기
for i in range(len(two_d)):
    for j in range(len(two_d)[i]):
        if i < j:
            two_d[i][j], two_d[j][i] = two_d[j][i], two_d[i][j]


            
