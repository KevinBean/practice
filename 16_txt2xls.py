# coding = utf-8

import xlwt #xlrd 读xls文件; xlwt 写xls文件。
import json #使用json,有点简单有复杂的感觉

def load_data(file_path):
    f = open(file_path, 'r')
    return json.load(f)

def w2xls(data):

    xls = xlwt.Workbook()
    sheet = xls.add_sheet("student")

    for i in range(len(data)):
        sheet.write(i, 0, i+1)
        json_data = data[str(i+1)]
        for j in range(len(json_data)):
            sheet.write(i, j+1, json_data[j])


    xls.save('student.xls')

if __name__ == '__main__':
    data = load_data("student.txt")
    w2xls(data)