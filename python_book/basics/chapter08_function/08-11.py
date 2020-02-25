'''
8-11 不变的魔术师：修改你为完成练习 8-10 而编写的程序，在调用函数
make_great() 时，向它传递魔术师列表的副本。由于不想修改原始列表，请返回修改后
的列表，并将其存储到另一个列表中。分别使用这两个列表来调用 show_magicians() ，
确认一个列表包含的是原来的魔术师名字，而另一个列表包含的是添加了字样“the
Great”的魔术师名字
'''
def show_magicians(list_of_magicians):
    '''show magicians in list'''
    for magician in list_of_magicians:
        print(magician)


def make_great(list_of_magicians):
    '''make magicians great'''
    great_magicians = list_of_magicians
    for n in range(len(great_magicians)):
        list_of_magicians[n] = "the great " + great_magicians[n]
    return great_magicians


list_of_magicians = ['magicianA', 'magicianB', 'magicianC', ]
show_magicians(make_great(list_of_magicians[:]))
show_magicians(list_of_magicians)