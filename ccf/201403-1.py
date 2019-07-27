# 试题编号：	201403-1
# 试题名称：    相反数

N = int(input())
s = input()
count = 0
list_of_num = s.split(" ")
for i in range(N):
    for j in range(i+1, N):
        if int(list_of_num[i]) + int(list_of_num[j]) == 0:
            count += 1
print(count)


'''
代码长度    204B
编程语言	PYTHON
评测结果    正确
得分       100
时间使用	125ms
空间使用    8.640MB
'''
