## 순차 큐

## 함수

def isQueueFull():
    global SIZE, queue, front, rear
    # Case1. rear 뒤에 여유가 있는 경우
    if (rear != SIZE-1):
        return False
    # Case2. 완전히 꽉찬 경우
    elif (rear == SIZE-1 and front == -1):
        return True
    # Case3. rear는 끝이지만 앞쪽에 여유가 있는 경우
    elif (rear == SIZE-1 and front != -1):
        for i in range(front+1, SIZE, 1):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if (front == rear):
        return True
    else:
        return

def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print('큐가 꽉찼어유')
        return
    rear += 1
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐가 비었어유')
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return('식사손님==>', data )

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐가 비었어유')
        return
    return queue[front+1]



## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1


## 메인

# ** enQueue
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<--', queue, '<-- 입구')
# enQueue('재남')

# ** deQueue
retData = deQueue()
print('손님 이리로: ', retData)
retData = deQueue()
print('손님 이리로: ', retData)

print('출구<--', queue, '<-- 입구')

enQueue('재남')
print('출구<--', queue, '<-- 입구')

enQueue('정국')
print('출구<--', queue, '<-- 입구')

enQueue('길동')
print('출구<--', queue, '<-- 입구')

