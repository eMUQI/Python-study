'''
10-12 记住喜欢的数字：将练习 10-11 中的两个程序合而为一。如果存储了用户喜
欢的数字，就向用户显示它，否则提示用户输入他喜欢的数字并将其存储到文件中。运
行这个程序两次，看看它是否像预期的那样工作。
'''

import json


def get_stored_number():
    try:
        with open("favorite_number.json") as f_obj:
            return json.load(f_obj)
    except FileNotFoundError:
        return None


def get_new_number():
    favorite_number = input("What is your favorite number?")
    with open("favorite_number.json", "w") as f_obj:
        json.dump(favorite_number, f_obj)


def main():
    favorite_number = get_stored_number()
    if favorite_number:
        print("I know your favorite number! It’s "+favorite_number)
    else:
        get_new_number()


main()
