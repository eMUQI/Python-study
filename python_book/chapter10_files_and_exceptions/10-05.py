'''
10-5 关于编程的调查：编写一个 while 循环，询问用户为何喜欢编程。每当用户输
入一个原因后，都将其添加到一个存储所有原因的文件中。
'''


with open("reasons.txt","a")as file:
    i=3
    while i>0:
        i -= 1
        file.write(input("The reason you like python:")+"\n")
