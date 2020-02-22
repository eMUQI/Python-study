'''
10-4 访客名单：编写一个 while 循环，提示用户输入其名字。用户输入其名字后，
在屏幕上打印一句问候语，并将一条访问记录添加到文件 guest_book.txt 中。确保这个
文件中的每条记录都独占一行。
'''


with open("guest.txt", "a")as file:
    i = 3
    while i > 0:
        i -= 1
        guest = input("Please enter your name:")
        file.write(guest+"\n")
        print("Welcome "+guest)
