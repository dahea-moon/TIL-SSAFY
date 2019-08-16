arr = [
    [5, 10, 4, 2, 5], [5, 2, 4, 5, 9], [1, 6, 9, 10, 8],
    [2, 5, 7, 1, 8], [3, 7, 4, 9, 8]
    ]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
new_arr = [[0]*5 for i in range(5)]

for x in range(len(arr)):
    for y in range(len(arr[x])):
        N = 0
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            if 0 <= testX <= 4:
                if 0 <= testY <= 4:
                    N += abs(arr[x][y] - arr[testX][testY])
        new_arr[x][y] = N

print(arr)
print(new_arr)
