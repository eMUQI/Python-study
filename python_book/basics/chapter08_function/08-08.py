'''
8-8 用户的专辑：在为完成练习 8-7 编写的程序中，编写一个 while 循环，让用户
输入一个专辑的歌手和名称。获取这些信息后，使用它们来调用函数 make_album() ，并
将创建的字典打印出来。在这个 while 循环中，务必要提供退出途径。
'''


def make_album(singer, album, songs_number=""):
    if songs_number:
        return {'singer': singer, 'album': album, 'songs_number': songs_number}
    else:
        return {'singer': singer, 'album': album}


while True:
    print(60*"#", end="\n")
    print("Please enter singer name and album name:(songs number is optional)")
    print("You can quit anytime by enter 'q'")
    singer = input("singer name:")
    if singer == "q":
        break
    album = input("album name:")
    if album == "q":
        break
    songs_number = input("songs_number:")
    if songs_number == "q":
        break
    print(make_album(singer, album, songs_number))
