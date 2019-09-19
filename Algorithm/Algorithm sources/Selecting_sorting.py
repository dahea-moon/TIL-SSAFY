# k번째로 작은 원소를 찾는 알고리즘
def select(arr, k):
    for i in range(0, k):
        min_idx = i
        for j in range(i+1, len(arr)):
            min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr[k-1]

# 선택 정렬
def selection_sort(arr):
    for i in range(0, len(arr)-1):
        min_idx = i 
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]