data = [0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,0,0,1,1,1]

for i in range(0, len(data)-6, 7):
    bite = data[i:i+7]
    result = 0
    for idx, val in enumerate(bite):
        if val:
            result += val<<(6-idx)

    print(result)
        