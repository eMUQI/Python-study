bicycles = ['terk','cannondale','redine','specialized']    #与C语言类似
print(bicycles)
print(bicycles[0].title())

print("bicycles[-1]:")
print(bicycles[-1].title())                   #当索引为-1时即访问最后一个元素
print()

print("修改元素后：")
bicycles[2] = 'redline'                      #修改元素
print(bicycles)
print()

print("bicycles.append('just_a_bike'):")
bicycles.append('just_a_bike')               #在列表末尾添加元素
print(bicycles)
print()

print("insert:")
bicycles.insert(0,'other_bike')              #在列表中插入元素(在n处添加空间，并将值储存在该位置)
print(bicycles)
print()

print("del:")
del bicycles[0]                              #删除指定索引元素(后面元素自动前移)
print(bicycles)
print()

print("pop:")
temp=bicycles.pop()                          #默认弹出最后一个元素，可加参数弹出指定元素
print(bicycles)
print(temp)
print()

print("remove:")                             #根据元素的值删除指定元素
bicycles.remove("redline")
print(bicycles)
