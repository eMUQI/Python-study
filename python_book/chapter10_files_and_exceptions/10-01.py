'''
10-1 Python 学习笔记：在文本编辑器中新建一个文件，写几句话来总结一下你至
此学到的 Python知识，其中每一行都以“In Python you can”打头。将这个文件命名为
learning_python.txt，并将其存储到为完成本章练习而编写的程序所在的目录中。编写一
个程序，它读取这个文件，并将你所写的内容打印三次：第一次打印时读取整个文件；
第二次打印时遍历文件对象；第三次打印时将各行存储在一个列表中，再在 with 代码
块外打印它们。
参考链接:
- https://stackoverflow.com/questions/10772947/attempting-to-read-open-file-a-second-time-gets-no-data
- https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects

'''


with open("./learning_python.txt") as file:
    # first print
    print(50*'#')
    content = file.read()
    print(content)
    print(50*'#', end="\n\n")
    # second print
    file.seek(0)
    for line in file:
        print(line.rstrip())
    print(50*'#')
    # third
    file.seek(0)
    lines = file.readlines()
    s = ""
    for line in lines:
        s += line

print(s)