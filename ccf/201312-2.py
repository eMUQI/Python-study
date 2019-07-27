#试题编号： 201312-2
#试题名称：	ISBN号码

s = input()
s_list = s.split("-")
s_new = "".join(s_list)

sum = 0
for i in range(len(s_new)-1):
    sum = sum + int(s_new[i])*(i+1)
if (sum % 11 == 10 and s_new[-1] == "X") or (s_new[-1] != "X" and int(s_new[-1]) == sum % 11):
    print("Right")
else:
    if sum % 11 == 10:
        print(s[0:-1]+"X")
    else:
        print(s[0:-1]+str(sum % 11))


'''
代码长度    351B
编程语言	PYTHON
评测结果    正确
得分       100
时间使用	31ms
空间使用    8.683MB
'''
