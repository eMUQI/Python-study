import json
import xlwt
import os


def readJson(file):
    with open(file, 'r', encoding='utf-8-sig') as fr:
        data = json.load(fr)
    return data


path = input("file path:")

dir_list = os.listdir(path)
print(dir_list)

for filename in dir_list:
    if len(filename) >= 5 and filename[-5:] == ".json":
        print(path + filename)
        data = readJson(path + filename)

        title = list(data[0].keys())  # 获取标题
        book = xlwt.Workbook()  # 创建一个EXCEL对象
        sheet = book.add_sheet('Sheet1', cell_overwrite_ok=True)  # 添加一个sheet页

        for i in range(len(title)):
            sheet.write(0, i, title[i])  # 写入标题

        for i in range(1,len(data)):
            single_data = data[i]

            for j in range(len(title)):
                if title[j] in  list(single_data.keys()):
                    sheet.write(i,j,single_data[title[j]]) #写入对应的值
        
        book.save(path + filename[:-4]+"xls")
        print(path + filename[:-4]+"xls Saved")
