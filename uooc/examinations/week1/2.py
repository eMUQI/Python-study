'''
数值运算
描述
获得用户输入的一个字符串，格式如下：‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬
M OP N‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬
其中，M和N是任何数字，OP代表一种操作，表示为如下四种：+, -, *, /（加减乘除）‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬
根据OP，输出M OP N的运算结果，统一保存小数点后2位。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‮‬
注意：M和OP、OP和N之间可以存在多个空格，不考虑输入错误情况。
'''

''' 我的答案
s = input()
if "+" in s:
    temp = s.split("+")
    # first number
    fn = float(eval(temp[0].strip()))
    # second number
    ln = float(eval(temp[1].strip()))
    result = fn+ln
elif "*" in s:
    temp = s.split("*")
    fn = float(eval(temp[0].strip()))
    ln = float(eval(temp[1].strip()))
    result = fn*ln
elif "/" in s:
    temp = s.split("/")
    fn = float(eval(temp[0].strip()))
    ln = float(eval(temp[1].strip()))
    result = fn/ln
elif "-" in s:
    temp = s.split("-")
    if s[0] != "-":
        fn = float(eval(temp[0].strip()))
        ln = float(eval(temp[1].strip()))
        result = fn-ln
    else:
        result = -fn-ln
print("{:.2f}".format(result))
'''

#参考答案
s = input()
print("{:.2f}".format(eval(s)))

