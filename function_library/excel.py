# -*- coding:UTF-8 -*-
import xlrd
#读取excel中单元格的数据
def readDate(filePath,sheetName,lineNum,columnNum):
	#打开excel文件
	data = xlrd.open_workbook(filePath)
	#获取工作表
	table = data.sheet_by_name(sheetName)
	#返回单元格值
	return table.cell(lineNum,columnNum).value

#读取excel中行数
def readDateRows(filePath,sheetName):
	#打开excel文件
	data = xlrd.open_workbook(filePath)
	#获取工作表
	table = data.sheet_by_name(sheetName)
	#返回行数
	return table.nrows

#读取excel中列数
def readDateCols(filePath,sheetName):
	#打开excel文件
	data = xlrd.open_workbook(filePath)
	#获取工作表
	table = data.sheet_by_name(sheetName)
	#返回列数
	return table.nclos

#写入excel 数据
def putData(filePath,sheetName,lineNum,columnNum,value):
	#打开excel文件
	data = xlrd.open_workbook(filePath)
	#获取工作表
	table = data.sheet_by_name(sheetName)
	#写入数据
	# ctype = 1	# 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
	# xf = 0 		#扩展的格式化 (默认是0)
	table.put_cell(lineNum,columnNum,value)

#print readDate("D:\\worksp\\config.xls", "Sheet1", 1, 0)
def readlinesValue(filePath,sheetName,lineNum):
	#打开excel文件
	data = xlrd.open_workbook(filePath)
	#获取工作表
	table = data.sheet_by_name(sheetName)
	#返回某一行的值
	return table.row_values(lineNum)

def readColValue(filePath,sheetName,col):
	#打开excel文件
	data = xlrd.open_workbook(filePath)
	#获取工作表
	table = data.sheet_by_name(sheetName)
	#返回某一列的值
	return table.col_values(col) 

