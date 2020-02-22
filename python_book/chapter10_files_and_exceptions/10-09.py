'''
10-9 沉默的猫和狗：修改你在练习 10-8中编写的 except 代码块，让程序在文件不
存在时一言不发。
'''


try:
    with open("cats.txt") as file1:
        print(file1.read())
    with open("dogs.txt") as file2:
        print(file2.read())
except FileNotFoundError:
    pass
