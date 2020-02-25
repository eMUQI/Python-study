'''
10-6 加法运算：提示用户提供数值输入时，常出现的一个问题是，用户提供的是
文本而不是数字。在这种情况下，当你尝试将输入转换为整数时，将引发 TypeError 异
常。编写一个程序，提示用户输入两个数字，再将它们相加并打印结果。在用户输入的
任何一个值不是数字时都捕获 TypeError 异常，并打印一条友好的错误消息。对你编写
的程序进行测试：先输入两个数字，再输入一些文本而不是数字。
'''
'''
题目可能出错
传入参数的类型错误 (例如在要求 int 时却传入了 list) 应当导致 TypeError，但传入参数的值错误 (例如传入要求范围之外的数值) 则应当导致 ValueError。
https://docs.python.org/zh-cn/3/library/exceptions.html?highlight=typeerror#TypeError
'''


try:
    a = int(input("Please enter a integer 'a':"))
    b = int(input("Please enter a integer 'b':"))
    print("a+b=%s" % str(a+b))
except ValueError:
    print("Make sure you enter a integer")
