names = ["王","赵","李","孙"]

print(names)
print()

names.append("钱")
print(names)
print()

names.insert(0,"邓")
print(names)
print()

names2=["老狐狸","老油条"]
print(names)
print(names2)
names.extend(names2)            #names=names+names2
print(names)

#pop(n)         弹出下标为n的元素，不填为-1
#remove(str)    删除与str匹配的第一个元素
#del list[n]    删除指定下标元素

#if xxx in list
#if xxx not in list
