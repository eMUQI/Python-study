def printit():              #定义
    print(35*"=")
    print("hello world")
    print(35*"=")

def prints():
    print(1*"*")
    print(2*"*")
    print(3*"*")
    print(4*"*")
    print(6*"*")

def sum_2num0():
    a = int(input("a:"))
    b = int(input("b:"))
    print("%d+%d=%d"%(a,b,a+b))

def sum_2num(a,b,c):        #有参数有返回值
    return a+b+c


x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))

print("x+y+z=" + str(sum_2num(x,y,z)))

printit()                   #调用
prints()

sum_2num0()

def test():
    a=11
    b=22
    c=33
    d=[a,b,c]               #封装为列表返回
    return d

print(test())

