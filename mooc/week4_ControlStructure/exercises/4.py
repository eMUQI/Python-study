'''
00371587024715377
三位水仙花数
描述
"水仙花数"是指一个三位整数，其各位数字的3次方和等于该数本身。‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬

例如：ABC是一个"3位水仙花数"，则：A的3次方＋B的3次方＋C的3次方 = ABC。

请按照从小到大的顺序输出所有的3位水仙花数，请用"逗号"分隔输出结果。

'''

result = []
for i in range(100, 1000):
    a = int(str(i)[0])
    b = int(str(i)[1])
    c = int(str(i)[2])
    if a**3 + b**3 + c**3 == i:
        result.append(str(i))
print(",".join(result))
