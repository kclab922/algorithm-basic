### 이진 탐색 트리
# 루트보다 작은 값 왼쪽, 큰 값 오른쪽
# 엄청 빠른 탐색 가능!

## 함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


## 변수
memory = []
root = None # 얘가 핵심
current = None
nameAry = ['블핑','레벨', '에핑', '걸데', '트와', '마마무']

## 메인
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node) # 안 중요!

for name in nameAry[1:]: # ['레벨'....'마마무']
    node = TreeNode()
    node.data = name

    current = root 

    while True: # 무한반복(들어온 애가 자리잡을 때까지)
        if (name < current.data): # 레벨 < 블핑
            if (current.left == None):
                current.left = node
                break # 자리 잡음
            current = current.left ## 핵심
        else:
            if (current.right == None):
                current.right = node
                break # 자리 잡음
            current = current.right ## 핵심
    memory.append(node)


findName = '바바부'
current = root
while True:
    if (findName == current.data):
        print(findName, '찾았다 ^^')
        break
    elif (findName < current.data):
        if (current.left != None):
            print(findName, '없어요 ㅠ')
            break
        current = current.left
    else:
        if (current.right != None):
            print(findName, '없어요 ㅠ')
            break
        current = current.right