'''
10-11 喜欢的数字：编写一个程序，提示用户输入他喜欢的数字，并使用
json.dump() 将这个数字存储到文件中。再编写一个程序，从文件中读取这个值，并打
印消息“I know your favorite number! It’s _____.”。
'''

import json


def get_stored_number():
    with open("favorite_number.json") as f_obj:
        print(json.load(f_obj))


def get_new_number():
    favorite_number = input("What is your favorite number?")
    with open("favorite_number.json", "w") as f_obj:
        json.dump(favorite_number, f_obj)

