'''f = open("test1.txt")

str = f.read()

f1 = open("test1_backup.txt","w")

f1.write(str)

f.close()
f1.close()'''

old_file_name = input("请输入要复制的文件名：")

i = old_file_name.rfind(".")
temp = old_file_name[:i]+"_backup"+old_file_name[i:]

old_file = open (old_file_name)
new_file = open (temp,"w")

new_file.write(old_file.read())     #while True:
                                    #   content = old_file.read(1024)
                                    #   if len(content)==0:
                                    #       break
                                    #   new_file.write(content)

old_file.close()
new_file.close()

