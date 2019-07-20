a = [11,22,33]
b = [11,22,33]
c = [44,55]

print(a)
print(c)
print()

print("extend:")
a.extend(c)
print(a)
print()

print("append:")
b.append(c)             #无返回值，直接修改
print(b)
