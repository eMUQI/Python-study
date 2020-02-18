'''
9-14 骰子：模块 random 包含以各种方式生成随机数的函数，其中的 randint() 返回
一个位于指定范围内的整数，例如，下面的代码返回一个 1~6内的整数：
from random import randint
x = randint(1, 6)
请创建一个 Die 类，它包含一个名为 sides 的属性，该属性的默认值为 6。编写一
个名为 roll_die() 的方法，它打印位于 1和骰子面数之间的随机数。创建一个 6面的骰
子，再掷 10次。
创建一个 10面的骰子和一个 20面的骰子，并将它们都掷 10次
'''
from random import randint

class Die:
    def __init__(self,sides="6"):
        self.sides = sides
    def roll_die(self):
        print(randint(1,self.sides))

die6 = Die(6)
for i in range(10):
    die6.roll_die()
print(30*"#")

die10 = Die(10)
die20 = Die(20)
for i in range(10):
    die10.roll_die()
print(30*"#")

for i in range(10):
    die20.roll_die()