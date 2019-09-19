def babygin(arr, n, k):
    if k == n-1:
        chk_1 = arr[:3]
        chk_2 = arr[3:]
        if isrun(chk_2) and istriplet(chk_1):
            print('babygin')
        elif istriplet(chk_2) and isrun(chk_1):
            print('babygin')
        elif isrun(chk_1) and isrun(chk_2):
            print('babygin')
        elif istriplet(chk_2) and istriplet(chk_1):
            print('babygin')
        else:
            print('fail')
    else:
        for i in range(k, n-1):
            arr[i], arr[k] = arr[k], arr[i]
            babygin(arr, n, k+1)
            arr[i], arr[k] = arr[k], arr[i]

def istriplet(arr):
    if arr[0] == arr[1] == arr[2]:
        return True
    else:
        return False

def isrun(arr):
    cnt = 0
    if arr[2] - arr[1] == 1:
        cnt += 1
    if arr[1] - arr[0] == 1:
        cnt += 1
    if cnt == 2:
        return True
    else:
        return False

# babygin([1,2,4,7,8,3], 6, 0)
babygin([6,6,7,7,6,7], 6, 0)