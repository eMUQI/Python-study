'''
8-9 魔术师：创建一个包含魔术师名字的列表，并将其传递给一个名为
show_magicians() 的函数，这个函数打印列表中每个魔术师的名字。
'''


def show_magicians(list_of_magicians):
    '''show magicians in list'''
    for magician in list_of_magicians:
        print(magician)

list_of_magicians = ['magicianA','magicianB','magicianC',]
show_magicians(list_of_magicians)