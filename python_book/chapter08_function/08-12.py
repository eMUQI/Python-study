'''
8-12 三明治：编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个
函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点
的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参。
'''
def make_sanswitch(*toppings):
    """概述要制作的三明治"""
    print("Making a sandswitch with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_sanswitch("A","B","C","D")
make_sanswitch("a","b","c")
make_sanswitch("1","2")
