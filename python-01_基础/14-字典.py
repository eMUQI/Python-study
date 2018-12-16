info = {"name":"baby","age":18,"sex":"man"}     # 键:值     有一点点类似C#哈希表

print(info)
print()

print(info["name"])
print(info["age"])
print(info["sex"])
print()

info["isgay"]="No"             #增
print(info)
print()

info["isgay"]="Yes"             #改
print(info)
print()

del info["isgay"]               #删
print(info)
print()

print(info.get("isgay"))        #查
print(info.get("name"))
print()

print(len(info))                #键值对的个数
print(info.keys())
print(info.values())

