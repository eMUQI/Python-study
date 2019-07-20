#1.打印功能提示

print(35*"=")
print("      名字管理系统")
print("1.添加一个新的名字")
print("2.删除一个名字")
print("3.修改一个名字")
print("4.查询一个名字")
print("5.退出")
print(35*"=")

#2.获取用户输入
names=[]

#3.根据用户的选择，执行相应功能
while(True):
    num=int(input("请输入功能序号："))
    if num==1:
        new_names=str(input("请输入名字："))
        if new_names in names:
            print("该名字已存在！")
        else:
            names.append(new_names)
        print(names)
    elif num==2:
        delete_name=str(input("请输入要删除的名字："))
        if delete_name in names:
            names.remove(delete_name)
        else:
            print("输入的姓名不存在")
    elif num==3:
        change_name=str(input("请输入要更改的名字："))
        if change_name in names:
            n_name=str(input("请输入新名字："))
            if(n_name in names):
                print("该名字已存在！")
            else:
                names[names.index(change_name)]=n_name
        else:
            print("该名字不存在！")
    elif num==4:
        find_name=str(input("请输入要查询的名字："))
        if find_name in names:
            print("存在")
        else:
            print("不存在")
    elif num==5:
        break
    else:
        print("输入有误！")
