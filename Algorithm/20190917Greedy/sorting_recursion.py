def select_sorting(data, i, n):
    min_num = i
    if i == n:
        return
    for j in range(i+1, n):
        if data[j] < data[min_num]:
            min_num = j
    data[i], data[min_num] = data[min_num], data[i]
    select_sorting(data, i+1, n)


a = [1,3,5,4,2]
n = len(a)
select_sorting(a, 0, n)
print(a)
