# 2019-14505 엄세희


# sol.py
# answer 함수 작성
# range(i,j)는 j는 포함하지 않음을 명심한다.
# (초기화 -> 반복문 -> 사용) 순서를 기억한다.
# 급수의 시작점과 끝점을 변수화하여, 다른 숫자를 넣어 활용 가능하도록 만든다.



# 문제 1

def answer01() :
    total = 0
    start01 = 1 # 급수의 시작점
    end01 = 30 # 급수의 끝점
    for n in range(start01, end01 + 1):
        m = 1 / n
        total += m
    return total





# 문제 2
# answer02()의 경우 급수가 2개여서, 코드가 불필요하게 \
# 길어질 것을 우려하여 시작점과 끝점을 변수화시키지 않음

def answer02() :
    total = 0
    for n in range(1, 51):
        for m in range(1, 31):
            div = n / m
            total += div
    return total






# 문제 3

def answer03() :
    total = 0
    start03 = 0
    end03 = 99
    for k in range(start03, end03 + 1) :
        x = (1 / 100)*((k / 100)**2)
        total += x
    return total




