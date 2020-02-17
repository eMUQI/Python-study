'''
8-10 了不起的魔术师：在你为完成练习 8-9 而编写的程序中，编写一个名为
make_great() 的函数，对魔术师列表进行修改，在每个魔术师的名字中都加入字样“the
Great”。调用函数 show_magicians() ，确认魔术师列表确实变了。
'''


def show_magicians(list_of_magicians):
    '''show magicians in list'''
    for magician in list_of_magicians:
        print(magician)


def make_great(list_of_magicians):
    '''make magicians great'''
    for n in range(len(list_of_magicians)):
        list_of_magicians[n] = "the great " + list_of_magicians[n]


list_of_magicians = ['magicianA', 'magicianB', 'magicianC', ]
make_great(list_of_magicians)
show_magicians(list_of_magicians)
