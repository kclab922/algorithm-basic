# Ch3-2. 선형 리스트

## 함수
def add_data(friend):
    # 1단계: 빈칸 추가 
    katok.append(None)
    kLen = len(katok)
    # 2단계: 마지막 칸에 대입
    katok[kLen-1] = friend

def insert_data(position, friend): # 3, 미나
    # 1단계: 빈칸 추가
    katok.append(None)
    kLen = len(katok)
    # 2단계: 한칸씩 뒤로 이동
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    # 3단계: 빈칸에 대입
    katok[position] = friend

def delete_data(position):
    # 1단계: 지우기
    katok[position] = None
    kLen = len(katok)
    # 2단계: 한 칸씩 앞으로 이동
    for i in range(position+1, kLen, 1):
        katok[i-1] = katok[i]
        katok[i] = None
    # 3단계: 마지막 칸 자체를 제거
    del(katok[kLen-1])


## 변수
katok = []

## 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)

add_data('모모')
print(katok)

insert_data(3, '미나')
print(katok)

delete_data(4)
print(katok)




