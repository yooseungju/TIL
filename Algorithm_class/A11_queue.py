

SIZE = 4
Q = [0]*SIZE

rear = 0
front = 0

def isFull(Q):
    global  rear
    if rear == SIZE-1:
        return True
    else: return False

def isEmpty():
    if rear == front:
        return True
    else: return False

def enQueue(item):

    if isFull(Q):
        return "더 이상 담을 수 없습니다."
    else:
        rear = (rear + 1) % len(Q)
        Q[rear] = item

def deQueue():
    global rear
    global front
    if not isEmpty():
        return Q[front]
    else:
        front = (front+1)%len(Q)
        return Q[front]



enQueue(1)
enQueue(2)

print(deQueue())

print(Q)