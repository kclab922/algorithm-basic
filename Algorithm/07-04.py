### 원형 큐
# 전제: 원형 큐가 꽉 찬 상태는 한 칸이 반드시 비워진 상태. 
# 이유: 꽉 차면 front와 rear가 같으므로, 원형 큐가 꽉 찼는데도 빈 것과 같은 것으로 처리되므로

## 함수

def isQueueFull():
    global SIZE, queue, front, rear
    if ((rear+1)%SIZE == front):
        return True
    else:
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
    rear = (rear+1) % SIZE
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐가 비었어유')
        return
    front = (front+1) % SIZE
    data = queue[front]
    queue[front] = None
    return('식사손님==>', data )

def peek():
    global SIZE, queue, front, rear
    if (isQueueEmpty()):
        print('큐가 비었어유')
        return
    return queue[(front+1) % SIZE]



## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = 0


## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
print('출구<--', queue, '<--입구')
#
retData = deQueue()
print('손님 이리로 :', retData)
retData = deQueue()
print('손님 이리로 :', retData)

print('출구<--', queue, '<--입구')
#
enQueue('재남')
print('출구<--', queue, '<--입구')
enQueue('정국')
print('출구<--', queue, '<--입구')

enQueue('길동')
print('출구<--', queue, '<--입구')
