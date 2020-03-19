s = input()
temp = float(s[:-1])
if s[-1].upper() == "C":
    result = temp*1.8+32
    # print(str(round(result,2))+"F")
    print("%.2fF"%float(round(result,2)))
elif s[-1].upper() == "F":
    result = (temp-32)/1.8
    # print(str(round(result,2))+"C")
    print("%.2fC"%float(round(result,2)))
else:
    print("输入格式错误")
