
print("请输入年龄：")
age_s=input() #input()输入的值默认为字符串类型
age=int(age_s) #类型转换
               #使用 str(*) 转换为字符串 

#age=int(input())

if age>=18:         #冒号不可少！
    print("?")      #必须缩进 
    if(int(input())>0):
        print("go go go!")
    else:
        print("bye!")
#elif [条件]：
else:               #冒号不可少！
    print("!")      #必须缩进

print("\n\n例子：车票")

ticket =1     #1有0无
knifeLength=8 #cm

if ticket == 1:
    print("检测到车票，开始安检...")
    if(knifeLength<=10):
        print("通过安检，祝您乘坐愉快！")
    else:
        print("请在原地等待工作人员")
else:
    print("车票无效")

