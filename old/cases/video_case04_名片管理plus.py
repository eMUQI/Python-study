cards = []
while True:
    print(35*"=")
    print("名片管理系统")
    print("1.添加一个新的名片")
    print("2.删除一个名片")
    print("3.修改一个名片")
    print("4.查询一个名片")
    print("5.显示所有名片")
    print("6.退出")
    print(35*'=')

    num=int(input("请输入功能序号:"))

    if num == 1:
        new_name =input("请输入姓名：")
        new_email = input("请输入邮箱：")
        new_tel = input("请输入电话号码：")
        new_info = {"name":new_name,"email":new_email,"tel":new_tel}
        cards.append(new_info)

        print(cards)#for test
    elif num==2:
        del_name =input("请输入姓名：")
        for temp in cards:
            if temp["name"]==del_name:
                break


    elif num==3:
        pass
    elif num==4:
        find_name=input("请输入姓名：")
        flag=0
        for temp in cards:
            if find_name == temp["name"]:
                print("姓名\t邮箱\t电话号码\t")
                print("%s\t%s\t%s\t"%(temp["name"],temp["email"],temp["tel"]))
                flag=1
        if flag==0:
            print("未找到%s"%find_name)
    elif num==5:
        print("姓名\t邮箱\t电话号码\t")
        for temp in cards:
            print("%s\t%s\t%s\t"%(temp["name"],temp["email"],temp["tel"]))
    elif num==6:
        break
    else:
        print("输入有误请重新输入！")
