cards = [{"name":"baby","age":18},{"name":"baby2","age":17}]

find_name = input("who?")

for temp in cards:
    if find_name == temp["name"]:
        print("found it !")
        break
else:                                   #若for循环内没有break则执行 
    print("do not know!")

