'''
9-13 使用 OrderedDict ： 在练习 6-4中，你使用了一个标准字典来表示词汇表。请
使用 OrderedDict 类来重写这个程序，并确认输出的顺序与你在字典中添加键 — 值对的
顺序一致。
'''
from collections import OrderedDict

favorite_fruits = OrderedDict()
favorite_fruits["A"] = "apple"
favorite_fruits["B"] = "banana"
favorite_fruits["C"] = "orange"

for person, fruit in favorite_fruits.items():
    print(person, fruit)
