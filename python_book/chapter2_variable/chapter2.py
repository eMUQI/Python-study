name = "Ada Lovelace"

#使用方法修改字符串大小
print(name.title())
print(name.upper())
print(name.lower())
print()
 
# 合并（拼接）字符串
first_name = "ada"
last_name = "lovelace"
full_name = first_name + last_name

print(full_name + "\n")
print("Hello,"+ full_name.title())

message = "Hello, " + full_name.title() + "!"
print(message)
print("\n\n")

#利用制表符或换行符来添加空白
print("Python")
print("\tPython\n")
print("Language:\n\tPython\n\tC\n\tJavaScript")

#删除空白
favorite_language = '    python'
print(favorite_language)
print(favorite_language.strip())
