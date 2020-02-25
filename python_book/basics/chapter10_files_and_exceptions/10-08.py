'''
10-8 猫和狗：创建两个文件 cats.txt和 dogs.txt，在第一个文件中至少存储三只猫的
名字，在第二个文件中至少存储三条狗的名字。编写一个程序，尝试读取这些文件，并
将其内容打印到屏幕上。将这些代码放在一个 try-except 代码块中，以便在文件不存
在时捕获 FileNotFound 错误，并打印一条友好的消息。将其中一个文件移到另一个地
方，并确认 except 代码块中的代码将正确地执行。
'''


try :
    with open("cats.txt") as file1:
        print(file1.read())
    with open("dogs.txt") as file2:
        print(file2.read())
except FileNotFoundError:
    print("can't find your file")
