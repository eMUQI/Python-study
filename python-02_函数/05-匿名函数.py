info = [{"name":"a","age":"20"},{"name":"c","age":"19"},{"name":"b","age":"27"}]
print(info)
print()
info.sort(key=lambda x:x['name'])
print(info)
print()
info.sort(key=lambda x:x['age'])
print(info)
print()

print(70*"=")
def test(a,b):
    result =a+b
    return result

def test1(a,b,func):
    result = func(a,b)
    return result

num = test(11,22)
print(num)
num1 = test1(11,22,lambda x,y:x+y)
print(num1)
num1 = test1(11,22,lambda x,y:x-y)
print(num1)
print()

print(70*"=")

#fun_new = input("请输入一个匿函数：")
#fun_new = eval(fun_new)
#num1 = test1(11,22,lambda x,y:x*y )

