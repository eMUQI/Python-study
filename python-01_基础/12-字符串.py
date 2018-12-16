a=100
c=150
print("a=%d,c=%d\ta+c=%d"%(a,c,a+c))
print()

i="love"
j="you"
print("i=%s,j=%s\ti+j=%s"%(i,j,i+j))        #字符串组合
print()

t=i+j
f="===%s==="%t                              #字符串组合
print(f)
print()

f=f+"$"
print(f)
print("f[5]="+f[5])                         #字符串下标
print("f[-1]="+f[-1])
print()

print(t)
print("t[2:4]=%s"%t[2:4])                   #字符串切片（不包含最后一个）
print("t[2:]=%s"%t[2:])                     #起始位置到最后
print("t[2::2]=%s"%t[2::2])                 #跳着
print("t[::-1]=%s"%t[::-1])             #逆序输出
print()

s='hello world, amazing world!'
print(s)
print('s.find("world")=%s'%s.find("world"))
print('s.rfind("world")=%s'%s.rfind("world"))
print('s.find("hi")=%s'%s.find("hi"))               #找不到返回-1
print('s.index("world")=%s'%s.index("world"))       #找不到报警告
print('s.rindex("world")=%s'%s.rindex("world"))
print("s.count('world')=%s"%s.count("world"))


