a=100
b=a

print(id(a))
print(id(b))

a=a+1           #不可变类型
print(id(a))
print(id(b))

A = [11,22,33]  #可变类型
B = A

print()
print(A)
print(B)

A.append(55)
print(A)
print(B)



