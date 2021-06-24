# 2019-14505 엄세희
# Loop Over List -- Basic Programming Patterns 
#

# Suppose you are given a list of numbers
xs = [62, 47, 86, 117, 48, 37, 73, 41, 27, 92, 
      37, 47, 19,  25, 70, 46, 52, 51, 14, 4]


# 1. Summation 
# Compute sum of xs. Do NOT use the built-in function sum()
total = 0
for i in xs:
    total += i

print(total)



# 2. Counting
# How many even numbers in xs?
total = 0
for i in xs:
    if i % 2 == 0:
        total +=1
print(total)

    
    


# 3. Searching
# Find the index of 73
for i, x in enumerate(xs):
    if x == 73:
        break
print(i)

#------loop over list 영상 참조------------------------
# Find the index of first 73
search = 73

for i, x in enumerate(xs):
    if x == search:
        index = i
        break
print(index)

# Find the index of last 73
search = 73

for i, x in enumerate(xs):
    if x == search:
        index = i
print(index) # break을 빼주면 index에 계속해서 새로운 i가 씌워져서 마지막 i가 프린트?

#만약에 list에 없는 값을 search에 넣으면 어떻게 되나?
#------------------------------------------------------



# 4. Sorting
# Find the maximum. Do NOT use the built-in function max()
for a in xs: #이게 왜 안되는지 모르겠습니다
    for b in xs:
        if a > b:
            continue
    print(b)
            
#-----------------------------------------------------
maximum = xs[0]
for x in xs: #xs 대신 xs[1:], (첫번째부터 끝까지라는 뜻)쓸 수 있음
    if maximum < x:
        maximum = x #맥시멈 교체

print(maximum)
#------------------------------------------------------


# 5. Mapping 
# Create a list of x*x for all x in xs
a = []
for x in xs:
    for y in xs:
        a = x * y
    a.append(a)
print(a)

#-----------------------------------------------------
#아예 문제 잘못해석함..
squares = []
for x in xs:
    sq = x*x
    squares.append(sq)
#    print(x,squares)-> 이렇게 하면 여러개의 행에 걸쳐서 점점 x의 제곱이 쌓이는 것을 확인가능

print(squares)
#------------------------------------------------------


# 6. Filtering
# Filter even numbers in xs, i.e. select even numbers from xs
# and create a new list.

a=[x for x in xs if x % 2 ==0] #이 방법 이외에도 리스트를 만드는 방법이 있나요?
print(a)


#-------------------------------------------------------
evens = []
for x in xs:
    if x % 2 == 0:
        evens.append(x)
print(evens)
#--------------------------------------------------------
        

