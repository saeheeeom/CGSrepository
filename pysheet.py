# pysheet.py
# 2019-14505 엄세희

from collections import Counter
import sys


def colnames(filename): # 첫 행의 컬럼 이름 추출
    file = open(filename)
    firstline = file.readline()
    colnames = firstline.strip().split()
    ans = ''
    for i in range(len(colnames)):
        ans += colnames[i] + " "
    return ans





def subtotal(value_colname, group_colname, filename, calc):
    file = open(filename)
    firstline = file.readline()
    colnames = firstline.strip().split()

    for num, colname in enumerate(colnames):
        if colname == value_colname:
            valnum = num
        elif colname == group_colname:
            grpnum = num

    total = {}
    count = {}
    
    for line in file :
        data = line.strip().split()
        data[valnum] = float(data[valnum])
        total[data[grpnum]] = total.get(data[grpnum],0) + data[valnum]
        count[data[grpnum]] = count.get(data[grpnum],0) + 1 # 평균 내기 위한 개수세기

    ans = ''    
    for key in total:
        if calc == 'mean':
            ans += '{:<10}{:>10.3f}\n'.format(key, total[key]/count[key])
        if calc == 'sum':
            ans += '{:<10}{:>10.3f}\n'.format(key, total[key])
    return ans
    




def colsums(column_range, filename, calc):
    file = open(filename)
    firstline = file.readline()
    colnames = firstline.strip().split()
    startcol = int(column_range.split('-')[0]) # 범위 구하기
    endcol = int(column_range.split('-')[1])
    
    count = 0
    total = {}
    for line in file:
        count += 1
        data = line.strip().split()
        
        for i in range(startcol-1, endcol):
            total[colnames[i]] = total.get(colnames[i], 0) + float(data[i])                    
    ans = ''    
    for key in total :
        if calc == 'sum':
            ans += '{:<10}{:>10.3f}\n'.format(key, total[key])
        if calc == 'mean':
            ans += '{:<10}{:>10.3f}\n'.format(key, total[key]/count)
    return ans
            




def table(colname, filename): # Counter() 이용하기
    freq = Counter()
    file = open(filename)
    firstline = file.readline()
    colnames = firstline.strip().split()

    for num, col in enumerate(colnames):
        if col == colname:
            colnum = num
    countlist = [] # 개수 세기 위해 전체 data 넣은 list 만들기
    for line in file:
        data = line.strip().split()
        countlist.append(data[colnum])
    for data in countlist:
        freq[data] += 1
    total = ''
    for key in freq:
        ans = '{:<10}{:>10}\n'.format(key, freq[key])
        total += ans
    return total





def sortby(colname, filename): # 먼저 이름을 key로 하여 정렬기준컬림 정렬
    file = open(filename)
    firstline = file.readline()
    colnames = firstline.strip().split()
    
    for num, col in enumerate(colnames):
        if col == colname :
            stdnum = num
    cdict = {}    
    orgdict = {}
    for line in file:
        data = line.strip().split()
        orgdict[data[0]] = line
        cdict[data[0]] = data[stdnum]
        sortcol = sorted(cdict.items(), key = lambda x:x[1])
    
    ans = ''
    
    for sorttuple in sortcol: # 나머지 컬럼을 정렬순서에 맞춰서 추가
        ans += orgdict[sorttuple[0]]
    
    return ans
    



def frequency(colname, ninterval, filename):
    file = open(filename)
    firstline = file.readline()
    colnames = firstline.strip().split()
    ninterval = int(ninterval)

    for i, col in enumerate(colnames):
        if col == colname:
            colnum = i
    
    countcolumn = []
    length = 0
    for line in file:
        length += 1
        data = line.strip().split()
        countcolumn.append(data[colnum])

    start = float(min(countcolumn))
    end = float(max(countcolumn))
    countbrk = start
    breaks = [start] # break개수 = 구간 개수 + 1
    for i in range(ninterval):
        space = (end - start) / ninterval
        countbrk += space
        breaks.append(countbrk)
        
    counts = []
    startCount = 0
    for data in countcolumn:
        data = float(data) # 각 구간에 속한 데이터 개수세기
        if round(breaks[0],1) <= data <= round(breaks[1],1):
            startCount += 1
    counts.append(startCount)

    
    for i in range(1, ninterval):
        count = 0
        for data in countcolumn:
            data = float(data)
            if round(breaks[i],1) < data <= round(breaks[i+1],1):
                count += 1
        counts.append(count)
    freqDict = {'breaks': breaks, 'counts': counts}
    return freqDict    



   
def datatype(x):
    try:
        float(x)
        return float
    except ValueError:
        return str

def addcol(formula, filename): # 왜 안되는지 모르겠습니다
    file = open(filename)
    firstline = file.readline()
    colnames = firstline.strip().split()
    
    code = formula.strip().split()
    fml = ''
    for i in code:
        if datatype(i) == int:
            i = i
        elif datatype(i) == str:
            for num in range(len(colnames)):
                if i != colnames[num]:
                    i = i
                if i == colnames[num]:
                    val = num
                    for line in file:
                        data = line.strip().split()
                        i = data[num]
                
                
        fml += i
    return fml

    
    

                
                    
    
    #total = ''

    for line in file:        
        data = line.strip().split()
        for i, text in enumerate(colnames):
            if datatype(data[i]) is float:
                data[i] = float(data[i])
            colnames[i] = data[i]
        data.append(eval(formula))
        ans = ''
        for text in data:
            ans += str(text) + '   '
        total += ans + '\n'
    #return total

        

def plot(xcolname, ycolname, filename): # 미완성입니다
    file = open(filename)
    firstline = file.readline()
    colnames = firstline.strip().split()
    xinterval = 4
    yinterval = 20

    for i, col in enumerate(colnames):
        if col == xcolname:
            xnum = i
        elif col == ycolname:
            ynum = i
    
    xlist = []
    length = 0
    for line in file:
        length += 1
        data = line.strip().split()
        xlist.append(data[xnum])

    ylist = []
    length = 0
    for line in file:
        data = line.strip().split()
        ylist.append(data[ynum])


    xstart = float(min(xlist))
    xend = float(max(xlist))
    xbrk = xstart
    xbreaks = [xstart]
    for i in range(xinterval):
        space = (xend - xstart) / xinterval
        xbrk += space
        xbreaks.append(xbrk)

    ystart = float(min(ylist))
    yend = float(max(ylist))
    ybrk = ystart
    ybreaks = [ystart]
    for i in range(yinterval):
        space = (yend - ystart) / yinterval
        ybrk += space
        ybreaks.append(ybrk)
    
    rows = ''
    
    





if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'colnames' :
        filename = sys.argv[3]
        ans= colnames(filename)
        print(ans)

    if command == 'subtotal':
        calc = sys.argv[2]
        value_colname = sys.argv[3]
        group_colname = sys.argv[5]
        filename = sys.argv[7]
        ans = subtotal(value_colname, group_colname, filename, calc)
        print(ans)

    if command == 'colsums':
        column_range = sys.argv[2]
        filename = sys.argv[4]
        ans = colsums(column_range, filename, calc='sum')
        print(ans)
    elif command == 'colmeans':
        column_range = sys.argv[2]
        filename = sys.argv[4]
        ans = colsums(column_range, filename, calc='mean')
        print(ans)

    if command == 'table':
        colname = sys.argv[2]
        filename = sys.argv[4]
        ans = table(colname, filename)
        print(ans)

    if command == 'sort':
        colname = sys.argv[3]
        filename = sys.argv[5]
        ans = sortby(colname, filename)
        print(ans)     

    if command == 'frequency': # frequency 함수가 return한 값 활용하기
        colname = sys.argv[2]
        ninterval = sys.argv[3]
        filename = sys.argv[5]
        ans = frequency(colname, ninterval, filename)
        brklist = ans['breaks']
        cntlist = ans['counts']
        for i in range(int(ninterval)):
            print(round(brklist[i],1), ' - ', round(brklist[i+1],1), ' | ', cntlist[i])
    if command == 'hist' :
        colname = sys.argv[2]
        ninterval = sys.argv[3]
        filename = sys.argv[5]
        ans = frequency(colname, ninterval, filename)
        brklist = ans['breaks']
        cntlist = ans['counts']
        n = 60 / int(max(cntlist))
        for i in range(int(ninterval)):
            print(round(brklist[i],1), ' - ', round(brklist[i+1],1), ' | ', '*'*round(cntlist[i]*n))

    if command == 'addcol':
        formula = sys.argv[2]
        filename = sys.argv[4]
        ans = addcol(formula, filename)
        print(ans)       

    if command == 'plot':
        xcolname = sys.argv[2]
        ycolname = sys.argv[3]
        filename = sys.argv[5]
        ans = plot(xcolname, ycolname, filename)
        print(ans)   