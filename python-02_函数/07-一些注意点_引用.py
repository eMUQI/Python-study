a=100
b=[100]
c=[100]
def test(num):
    num+=num
    print(num)

def test1(num):
    num+=num
    print(num)

def test2(num):
    num = num + num
    print(num)

test(a)             #值没改变(不可变类型)
print(a)
print()

test1(b)            #值改变了(可变类型)
print(b)
print()

test2(c)            #num=num+num不等价于num+=num 
print(c)

