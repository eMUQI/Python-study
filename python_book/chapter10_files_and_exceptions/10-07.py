'''
10-7 加法计算器：将你为完成练习 10-6 而编写的代码放在一个 while 循环中，让
用户犯错（输入的是文本而不是数字）后能够继续输入数字。
'''


while True:

    print("Enter 'q' to quit")
    a = input("Please enter a integer 'a':")
    if a == "q":
        break
    b = input("Please enter a integer 'b':")
    if b == "q":
        break

    try:
        print("a+b=%s" % str(int(a)+int(b)))
    except ValueError:
        print("Make sure a and b both are integer")
