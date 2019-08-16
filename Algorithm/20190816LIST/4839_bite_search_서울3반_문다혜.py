import sys
sys.stdin = open("bitesearch_input.txt", "r")

T = int(input())

def binarySearch(key, low, high, count):
    if low > high:
        return False
    else: 
        middle = (low+high)//2
        if key == middle:
            return count
        elif key < middle:
            count += 1
            return binarySearch(key, low, middle, count)
        elif key > middle:
            count += 1
            return binarySearch(key, middle, high, count)


for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())

    A = binarySearch(Pa, 1, P, 0)
    B = binarySearch(Pb, 1, P, 0)

    if A-B == 0:
        win = 0
    elif A-B < 0:
        win = 'A'
    else:
        win = 'B'

    print("#{} {}".format(tc, win))
