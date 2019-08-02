#coding:utf-8

'''
Created on 2019��7��26��

@author: Administratofrom test.test_codecs import coding_checker
r
'''
import os
import xlrd
import datetime

namepath =os.chdir(r'E:\QQtemp\2549189581\FileRecv')

filename = "100G测试资源（视频 教程）免费获取.xlsx"

file = os.path.join(os.getcwd(),filename)

#打开文件

xl=xlrd.open_workbook(file)

#获取sheet

print(xl.sheet_names())

print(xl.sheets())

print(xl.nsheets)

print(xl.sheet_by_name('目录'))

print(xl.sheet_by_index(1))

#获取sheet内的汇总数据

table1=xl.sheet_by_name('目录')

print(table1.name)

print(table1.nrows)

print(table1.ncols)


'''四、单元格批量读取 '''

print(table1.row_values(0,1,4))  #合并单元格，显示首行值，其他为空

#print(table1.row(0,0,2))

print(table1.row_types(0))

#print(table1.row_slices(1,0,2))   #展示type和name

print(table1.col_values(0))

#特定单元格读取

print(table1.cell(1,2).value)

print(table1.cell_value(1,2))

print(table1.row(1)[2].value)

#取类型

print(table1.cell(1,2).ctype)

print(table1.cell_type(1,2))

print(table1.row(1)[2].ctype)

#六、(0,0)转换成A1

print(xlrd.cellname(0,0))

print(xlrd.cellnameabs(0,0))

print(xlrd.colname(30))

def read_excel(table1,row,col):
    
    name = table1.cell_value(row,col)
    
    type = table1.cell_type(row,col)
    
    if type == 0:
        
        name = "''"
        
    elif type == 1:
        
        name = name
        
    elif type == 2 and name %1 == 0:
        
        name =int(name)
        
    elif type == 3:
        
        #方法1：转换为日期时间
        
        #data_value = xlrd.xldate_as_datetime(name,0)
        
        #name = data_value
        
        #方法2：转换为元组
        
        date_value = xlrd.xldate_as_tuple(name,0)
        
        name = datetime(*date_value).strftime('%Y/%m/%d %H:%M:%S')
    
    elif type == 4:
        
        name = True if name ==1 else False
        
    return name
    

#七、获取表格内不同类型的name

print(table1.cell_value(1,1)) #数字2

print(table1.cell_type(1,1))

print(read_excel(table1,1,1))

print(table1.cell_value(0,1)) #数字0

print(table1.cell_type(0,1))

print(read_excel(table1,0,1))

#print(table1.cell_value(0,7)) #日期3

#print(table1.cell_type(0,7))

#print(read_excel(table1,0,7))

#print(table1.cell_value(0,8)) #布尔4

#print(table1.cell_type(0,8))

#print(read_excel(table1,0,))









































