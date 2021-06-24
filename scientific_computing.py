# scientific_computing.py
# 엄세희
# 2019-14505 

# 함수를 정의하기 이전 원형부터 만들어본다

import random # used for Monte Carlo Method




# sqrt function
# Compute the square root of a number using the Newton Method


# compute sqrt(2)
# find x such that x**2 = 2

# x[n+1] = x[n] - (x[n]**2 - 2) / (2 * x[n])
# x1 = x0 - (x0**2 - 2) / (2 * x0)
# x[1] = x[0] - ...
# x[2] = x[1] - ...
# x[3] = x[2] - ...

# 방법1 : 원하는 오차값의 범위가 설정되지 않은 경우
n = 10
x0 = 1
for i in range(n) :
    x1 = x0 - (x0**2 - 2) / (2 *x0)
    x0 = x1


# 방법2 : 원하는 오차값의 범위가 설정된 경우
n = 100
x0 = 1000
for i in range(n) :
    x1 = x0 - (x0**2 - 2) / (2 *x0)
    if abs(x1 -x0) < 1e-15 :
        break
    x0 = x1


# 방법3 : 2가 아닌 다른 숫자의 제곱근 구하기
# compute sqrt(y)
# find x such that x**2 = y

# x[n+1] = x[n] - (x[n]**2 - y) / (2 * x[n])
# x1 = x0 - (x0**2 - y) / (2 * x0)
#    = x0 - x0/2 + y / (2 * x0)
#    = x0/2 + y / (2 * x0)
#    = (x0 + y/x0) / 2


# 3-1 for문

def sqrt(y):
    n = 50
    x0 = y / 2
    for i in range(n) :
        x1 = (x0 + y/x0) / 2
        if abs(x1 - x0) < 1e-15:
            break

        x0 = x1
    return x1

x = sqrt(3)
y = sqrt(7)
print(x,y)

# 3-2 while문 (무한루프에 빠질 수 있어서 잘 안 쓰임)
y = 5
x0 = 2
while abs(y - x0**2) > 1e-15:
    x1 = (x0 + y/x0) / 2

    x0 = x1
    




# log function
# 테일러 정리
# z = x - 1 / x + 1
# log(x) = 2(z/1 + z**2/3 + z**5 / 5 + z**7/7 + ...)

n = 500
def log(x) :
    z = (x - 1) / (x + 1)
    sumY = 0
    for i in range(1, n) :
        y = (z**(2*i - 1))/(2*i - 1)
        sumY += y
    return 2 * sumY







# 몬테 카를로 방법
# import random module
# 원의 1/4 을 구한 뒤에 4배
# count / n : 사분원의 넓이
# dsq = distance square, 원점과 점의 거리의 제곱


# 함수 사용 x
n = 1000
count = 0
for i in range(n) :
    x = random.random()
    y = random.random()
    dsq = x**2 + y**2 
    if dsq < 1.0 :
        count += 1

ans = 4 * count / n

# 함수 사용 o

def calc_pi(n) :
    count = 0
    for i in range(n) :
        x = random.random()
        y = random.random()
        dsq = x**2 + y**2
        if dsq < 1.0 :
            count += 1
    
    ans = 4 * count / n
    return ans










# 수치 적분 numerical integration
# 각각의 넓이 구하는 방법을 area1, area2 의 함수로 표현


def area1(n):
    sum = 0
    for k in range(n):
        h = 1 / n
        area = h * ((k - 1)*h)**2
        sum += area
    return sum



def area2(n):
    sum = 0
    for k in range(n) :
        h = 1 / n
        area = h * (k * h)**2
        sum += area
    return sum






# 연습 2.12
# x = y**2
# y == ?

def sqrt(x):
    n = 2000
    g = x / 2
    for i in range(n) :
        g = (g + x/g) / 2
        if abs(g**2 - x) < 1e-15:
            break

        y = g
    return g
