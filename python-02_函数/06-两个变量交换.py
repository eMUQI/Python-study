a=1
b=0

#1
c=0
c=a
a=b
b=c
print("a=%d,b=%d"%(a,b))

#2
a=a+b
b=a-b
a=a-b
print("a=%d,b=%d"%(a,b))

#3
a,b = b,a
print("a=%d,b=%d"%(a,b))


