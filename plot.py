# 2019-14505 엄세희
# plot.py
# 파이썬으로 그래프 그리기
# list 활용
# 동영상 강의의 문제 & md의 문제 모두 포함



# matplotlib 패키지 설치, 사용하기
# 지정된 좌표의 점으로 그래프 그리기

import matplotlib.pyplot

matplotlib.pyplot.plot([1,2,3], [4,7,2]) # 그래프 생성
matplotlib.pyplot.plot([1,2,3], [3,6,4])
matplotlib.pyplot.show() # 그래프 화면으로 출력






# 함수 그래프 그리기
# y = f(x)
# 1. 초기화된 리스트에 
# 2. range 활용해서 
# 3. append로 좌표 채우기

xs = []
ys = []
for i in range(0, 101) :
    x = i / 100
    y = x**2
    xs.append(x)
    ys.append(y)

matplotlib.pyplot.plot(xs,ys) # 그래프 생성
matplotlib.pyplot.show() # 그래프 화면으로 출력






# x의 구간 지정해서 그래프 그리기
# -1 < x < 1
# 한 칸의 길이는 2 / 100

xs = []
ys = []
for i in range(0, 101) :
    x = -1 + 2 * i / 100
    y = x**2
    xs.append(x)
    ys.append(y)

matplotlib.pyplot.plot(xs, ys)
matplotlib.pyplot.show()






# 일반화한 그래프 그리기
# 일반화 하는 것 : x의 범위, 구간의 개수, 함수 f(x)

# xmin < x < xmax
# n : number of intervals
# plot y = f(x)

xmin = -2
xmax = 1
n = 10
def f(x):
    return x**2 + 3*x + 1

xs = []
ys = []

for i in range(0,n + 1):
    x = xmin + (xmax - xmin) * i/n 
    y = f(x)
    xs.append(x)
    ys.append(y)

matplotlib.pyplot.plot(xs, ys)
matplotlib.pyplot.show()






# 다른 함수도 적용 가능

xmin = -2
xmax = 3
n = 100
def f(x):
    return 3*x**3 - x**2 + 3*x + 1

xs = []
ys = []

for i in range(0, n + 1):
    x = xmin + (xmax - xmin) * i/n 
    y = f(x)
    xs.append(x)
    ys.append(y)

matplotlib.pyplot.plot(xs, ys)
matplotlib.pyplot.show()








# 정규분포 밀도함수 곡선 그리기
# x~N(mu, sigma**2)
# mu : 평균, sigma : 표준편차
# 평균과 표준편차를 넣으면 되는 일반화된 프로그램 짜기

import math

xs = []
ys = []

def f(x, mu, sigma) :
    stndrdND = 1 / (math.sqrt(2 * math.pi * sigma**2)) * math.exp(-(x - mu)**2 / 2 * sigma**2)
    return stndrdND

mu = 0        # 평균, 표준편차 지정
sigma = 1

for i in range(0,101):
    x = -3 + 6 * i / 100
    y = f(x, mu, sigma)
    xs.append(x)
    ys.append(y)

matplotlib.pyplot.plot(xs,ys)
matplotlib.pyplot.show()







# 원 그리기

# 첫번째, 삼각함수 없이 푸는 방법
# x와 y가 모두 양수인 일사분면만 표시
# 나누는 구간의 숫자가 작은 경우, 찍히는 점이 중심점으로부터 등간격이 아님
# x**2 + y**2 = r**2

xs = []
ys = []
r = 1

for i in range(0, 6):
    x = 0 + r * i / 5
    y = math.sqrt(1 - x**2)
    xs.append(x)
    ys.append(y)

matplotlib.pyplot.plot(xs,ys)
matplotlib.pyplot.show()

# 두번째, 삼각함수를 이용해서 푸는 방법
# 한 바퀴를 모두 표시 가능, 찍히는 점은 중심점으로부터 등간격
# 회전 각도로 정의하기
# 반지름을 일반화 해보았다
# 삼각함수는 math module import 필요

# x**2 + y**2 = r**2
# y = math.sqrt(1- x**2)
# x = cos(t)
# y = sin(t)

# 0 <= t <= 2pi

xs = []
ys = []
r = 1

for i in range(0,101) :
    t = 2 * math.pi * i / 100
    x = r * math.cos(t)
    y = r * math.sin(t)

    xs.append(x)
    ys.append(y)


matplotlib.pyplot.plot(xs, ys)
matplotlib.pyplot.show()








# 하트 그리기
# x = 16sin**3(t) : sin함수의 제곱은 인자 뒤에 표시하기
# y = 13sincos(t) -5cos(2t) -2cos(3t) -cos(4t)

xs = []
ys = []

for i in range(0,101) :
    t = 2 * math.pi * i / 100
    x = 16 * math.sin(t)**3
    y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
    xs.append(x)
    ys.append(y)

matplotlib.pyplot.plot(xs, ys)
matplotlib.pyplot.show()









# 체질량지수(BMI) 상관도 그리기
# 몸무게(kg) : w
# 키(m) : h
# f(x) : bmi, 몸무게에 따른 키 함수
# bmiGraph(bmi) : bmi에 따른 그래프 만드는 함수

import matplotlib.pyplot
import math

def bmiGraph(bmi) :
    ws = [] # for문 이전 초기화 잊지 말 것
    hs = []
    for i in range(0,101) :
       
        def f(w) :
            return math.sqrt(w / bmi) * 100
        w = 20 + 100 * i / 100
        h = f(w)

        ws.append(w)
        hs.append(h)
    
    return matplotlib.pyplot.plot(ws,hs)

bmiGraph(18.5), bmiGraph(25), bmiGraph(30), bmiGraph(35), bmiGraph(40)
matplotlib.pyplot.show()






