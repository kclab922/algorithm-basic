# Ch4-2. 단순 연결 리스트

## 함수
class Node():
    def __init__(self):
        self.data = None
        self.link = None 

def printNodes(start):
    current = start
    print(current.data, end=' ')
    while (current.link != None):
        current = current.link
        print(current.data, end=' ')
    print()

def insertNode(findData, insertData):
    global memory, head, pre, current
    # Case1: (하필) 머리 앞에 삽입. 다현 앞에 화사 넣는 상황.
    if (findData == head.data):
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return 
    # Case2: 중간노드 앞에 삽입. 사나 앞에 솔라 넣는 상황.
    current = head
    while (current.link != None):
        pre = current 
        current = current.link
        if (current.data == findData):
            node = Node()
            node.data = insertData
            node.link = current 
            pre.link = node 
            memory.append(node)
            return
    # Case3: 존재하지 않는 노드 앞에 삽입. 재남 앞에 문별 넣는 상황. (재남 없으므로 문별은 맨뒤로)
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

def deleteNode(deleteData):
    global memory, head, pre, current
    # Case1: 하필 머리를 삭제. 다현 삭제
    if (deleteData == head.data):
        current = head
        head = head.link 
        del(current)
        memory.append(node)
        return
    # Case2: 중간노드를 삭제. 쯔위 삭제
    current = head
    while (current.link != None):
        pre = current
        current = current.link
        if (current.data == deleteData):
            pre.link = current.link
            del(current)
            memory.append(node)
            return
    # Case3. 없는 노드를 삭제. 재남 삭제
    return

def findNode(findData):
    global memory, head, pre, current
    current = head
    # Case1. 머리가 찾는 애인 경우
    if (current.data == findData):
        return current
    # Case2. 찾는 애가 머리가 아닌 경우
    while (current.link != None):
        current = current.link
        if (current.data == findData):
            return current
    # Case3. 찾는 애가 없는 경우
    return Node() # 빈 노드 출력


## 변수
memory = []
head, pre, current = None, None, None
dataArray = ['다현', '정연', '쯔위', '사나', '지효'] # 내 데이터


## 메인
node = Node()
node.data = dataArray[0]
head = node
memory.append(node) # 생략 가능


for data in dataArray[1:]: # ['정연', '쯔위', ...]
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)

# insertNode('다현', '화사') # 찾을 데이터, 그 앞에 삽입할 데이터
# printNodes(head)

# insertNode('사나', '솔라') # 찾을 데이터, 그 앞에 삽입할 데이터
# printNodes(head)

# insertNode('재남', '문별') # 찾을 데이터, 그 앞에 삽입할 데이터
# printNodes(head)

# deleteNode('다현') # 삭제할 데이터
# printNodes(head)

# deleteNode('쯔위') # 삭제할 데이터
# printNodes(head)

# deleteNode('재남') # 삭제할 데이터
# printNodes(head)

retNode = findNode('쯔위')
print(retNode.data, '뮤비가 플레이 됩니다')