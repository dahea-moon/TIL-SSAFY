N = [1, 2, 4, 4, 2, 3, 5, 7, 3, 1, 6, 5, 7, 3, 8, 6]
datas = [N[i:i + 4] for i in range(0, 16, 4)]
raw = []

for data in datas:
    for y in range(data[1], data[3]):
        for x in range(data[0], data[2]):
            raw.append((x, y))

result = set(raw)
print(len(result))
