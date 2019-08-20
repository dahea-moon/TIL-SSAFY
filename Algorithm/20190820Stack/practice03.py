stack = [1]
visited = [True]*2 + [False]*6
numbers = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
route = [1]
matrix = [[0]*8 for _ in range(8)]

numbers = [numbers[i:i+2] for i in range(0, len(numbers)-1, 2)]
for number in numbers:
    matrix[number[0]][number[1]] = 1

while stack:
    for idx, val in enumerate(matrix[stack[-1]]):
        if val == 1 and visited[idx] == False:
            stack.append(idx)
            route.append(idx)
            visited[idx] = True
            break
    else:
        stack.pop(-1)

print(route)