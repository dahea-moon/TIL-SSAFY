queue = [0]*3
rear = -1
front = -1

def enque(item):
    global rear
    if rear > 2:
        pass
    else:
        rear += 1
        queue[rear] = item

def deque(item):
    global rear
    global front
    if rear == -1:
        pass
    else:
        front += 1
        return queue[front]

enque(1)
enque(2)
enque(3)
print(deque(0))
print(deque(1))
print(deque(2))
