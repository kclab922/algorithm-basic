### 재귀 호출 예제

# 팩토리얼 구하기
def fact(num):
    if num == 1:
        return 1
    return num * fact(num-1)
print(fact(5))
