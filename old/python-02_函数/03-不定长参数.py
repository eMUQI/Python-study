def test(a,b,*args):
    print(a)
    print(b)
    print(args)

def test2(*a):
    print(a)

def test3(*b):
    sum = 0 
    for temp in b:
        sum += temp
    print(temp)

def test4(a,b,c=33,*args,**kwargs): # *多出的没名字的  **多出的有名字的
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

test(1,2,3,4,5,6,7,8)
test(1,2)
test2(1,2,3)

test3(1,2,3,4,5)
test4(1,2,3,4,5,6,7,task=100,done=99)

A=(44,55,66)
B={"name":"kk","age":18}
print()
test4(1,2,3,A,B)
test4(1,2,3,*A,**B)

