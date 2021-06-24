# array.py
# 2019-14505 엄세희

class Vector:
    def __init__(self, *values):
        vecList = []
        for i in values:
            if type(i) is list:
                for x in i:
                    vecList.append(x)
            else:
                vecList.append(i)
        self.values = vecList


    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, values):
        self.__values = values


    def __repr__(self):
        return 'Vector{}'.format(tuple(self.values))


    def __len__(self):
        return len(self.values)


    def __getitem__(self, index):
        return self.values[index]


    def __setitem__(self, index, value):
        self.values[index] = value
        

    def __add__(self, other):
        newlist = []
        for i in range(len(self)):
            if type(other) == int:
                newlist.append(self[i] + other)
            else:
                a = len(self.values)
                b = len(other.values)
                if a == b :
                    newlist.append(self.values[i] + other.values[i])
                elif a > b:
                    for x in range(a//b):
                        for y in range(b):
                            newlist.append(self.values[x] + other.values[y])
                    for x in range(a%b):
                        newlist.append(self.values[b*(a//b)+x] + other.values[x])
                elif b > a:
                    for x in range(b//a):
                        for y in range(a):
                            newlist.append(self.values[x] + other.values[y])                   
                    for x in range(b%a):
                        newlist.append(other.values[a*(b//a)+x] + self.values[x])                    
        return newlist

    
    def __radd__(self, other):
        return self.__add__(other)


    def __mul__(self, other):
        newlist = []
        for i in range(len(self)):
            if type(other) == int:
                newlist.append(self[i] * other)
            else:
                a = len(self.values)
                b = len(other.values)
                if a == b :
                    newlist.append(self.values[i] * other.values[i])
                elif a > b:
                    for x in range(a//b):
                        for y in range(b):
                            newlist.append(self.values[x] * other.values[y])
                    for x in range(a%b):
                        newlist.append(self.values[b*(a//b)+x] * other.values[x])
                elif b > a:
                    for x in range(b//a):
                        for y in range(a):
                            newlist.append(self.values[y] * other.values[x]) 
                    for x in range(b%a):
                        newlist.aappend(other.values[a*(b//a)+x] * self.values[x])        
        return newlist

    def __rmul__(self, other):
        return self.__mul__(other)    


class Matrix:
    def __init__(self, *index):
        ans = []
        indexlist = list(index)
        for x in range(indexlist[0]-1):
            for y in range(indexlist[1]-1):
                ans.append(0.0)
        self.anslist = ans
    
    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, index):
        self.__index = index       

    def __repr__(self):
        return 'Matrix{}'.format(ans)

    def __getitem__(self, index):
        return ans[indexlist[1] * index [1] + index[0]]

    def __setitem__(self, index, value) :
        ans[indexlist[1] * index [1] + index[0]] = value
