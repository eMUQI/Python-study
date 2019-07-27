#试题编号:      201312-1
#试题名称：	出现次数最多的数

n = int(input())
s = input()

list_of_num = s.split(" ")
max = float("-inf")
result = float("inf")
for temp in list_of_num:
    i = list_of_num.count(temp)
    if i > max:
        max = i

for temp in list_of_num:
    if list_of_num.count(temp) == max and result > int(temp):
        result = int(temp)
print(result)

'''
代码长度    318B	
编程语言    PYTHON
评测结果    正确
得分       100
时间使用    62ms	
空间使用    8.714MB
'''