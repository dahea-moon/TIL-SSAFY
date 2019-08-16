import sys
sys.stdin = open("flatten_input.txt", "r")

T = 10
for tc in range(1, T+1):
    dumping = int(input())
    boxes = list(map(int,input().split()))
    count = 0

    while count < dumping:
        boxes = sorted(boxes)
        boxes[-1] -= 1
        boxes[0] += 1
        count += 1
    sorted(boxes)
    result = boxes[-1] - boxes[0]
    print("#{} {}".format(tc, result))