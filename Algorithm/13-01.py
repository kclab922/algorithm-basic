### 순차검색


## 함수
import random
def seqSearch(ary, fData):
    pos = -1
    for i in range(len(ary)):
        if (ary[i] == fData):
            post = i
            break
    return pos

## 변수
dataAry = [random.randint(30, 190) for _ in range(8)]
findData = random.choice(dataAry)

## 메인
print('배열-->', dataAry)
position = seqSearch(dataAry, findData)
if (position == -1):
    print(findData, '없어요 ㅠ')
else:
    print(findData, '는 ', position, '위치에 있어요.')