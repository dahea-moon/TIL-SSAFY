# 이진검색

# 구현
def binarySearch(a, key):
    start = 0
    end = len(a)-1
    
    while start <= end:
        middle = (start+end) // 2
        if a[middle] == key:
            return True
        elif a[middle] > key:
            end = a[middle] - 1
        else:
            start = a[middle] + 1
    return False

# 재귀함수 이용
def binarySearch2(a, key, low, high):
    if low > high:
        return False
    else:
        middle = (low + high) // 2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binarySearch2(a, key, low, middle-1)
        elif key > a[middle]:
            return binarySearch2(a, key, middle+1, high)