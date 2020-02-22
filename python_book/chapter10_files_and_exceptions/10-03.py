'''
10-3 访客：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写
入到文件 guest.txt中。
'''


with open("guest.txt", "w")as file:
    file.write(input("Please enter your name:"))
