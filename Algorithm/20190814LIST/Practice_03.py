arr = [[9, 20, 2, 18, 11], [19, 1, 25, 3, 21], [8, 24, 10, 17, 7], [15, 4, 16, 5, 6], [12, 13, 22, 23, 14]]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def isWall(testX, testY, i, h):
    if 0 <= testX < i and 0 <= testY < h:
        return True
    else:
        return False


for h in range(4):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            for x in range(i+1, len(arr)):
                for y in range(j+1, len(arr[i])):
                    minx = i + dx[h]
                    miny = j + dy[h]
                    testX = minx + x
                    testY = miny + y
                    if isWall(testX, testY, len(arr), len(arr[i])):
                        if arr[minx][miny] > arr[testX][testY]:
                            minx, miny = testX, testY
            arr[i][j], arr[minx][miny] = arr[minx][miny], arr[i][j]

print(arr)
