#试题编号:  201409-1
# 试题名称：	相邻数对

n = int(input())
s = input()
list_of_s = s.split(" ")
count = 0

for i in range(n-1):
    for j in range(i+1, n):
        if int(list_of_s[i])-int(list_of_s[j]) == 1 or int(list_of_s[i])-int(list_of_s[j]) == -1:
            count += 1

print(count)


'''
代码长度    306B
编程语言    PYTHON
评测结果    正确
得分       100
时间使用    812ms
空间使用    8.695MB
'''