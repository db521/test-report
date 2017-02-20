# -*- coding:UTF-8 -*-
import unittest,time,HTMLTestRunner,os,sys
sys.path.append("E:\\worksp\\function_library")
sys.path.append("E:\\worksp\\script")
from script import search 
from function_library import mail
from function_library import excel

#读取基础设置
case_path = excel.readDate("E:\\worksp\\config.xls", "Sheet1", 1,0) #用例路径
data_path = excel.readDate("E:\\worksp\\config.xls", "Sheet1", 1,1) #数据路径
report_path = excel.readDate("E:\\worksp\\config.xls", "Sheet1", 1,2) #结果路径

#读取用例 
case_path = case_path+"test_case.xls"
indxs = excel.readColValue(case_path,"test_case",0) #获取是否执行的标志
class_Name = excel.readColValue(case_path,"test_case",2)#获取脚本名称
test_Name = excel.readColValue(case_path,"test_case",3)#获取用例名称

#创建测试套件
testunit = unittest.TestSuite()
#循环读取数组中的用例
for i in range(0,len(indxs)):
	if indxs[i] == "Y":#判断是否执行
		#判断是否多个testcase
		if ";" in test_Name[i]:
			aaa = test_Name[i].split(";")
			for aa in aaa:
				testunit.addTest(unittest.makeSuite(eval(class_Name[i]),aa))
		else:	
			testunit.addTest(unittest.makeSuite(eval(class_Name[i]),test_Name[i]))#

now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))
filename = report_path+now+"result.html"
fp = open(filename,'wb')
runner = HTMLTestRunner.HTMLTestRunner(
	stream = fp,
	title = u"测试报告",
	description = u"用例执行结果"
	)

if __name__ == "__main__":
	#执行测试用例集
	runner.run(testunit)
	#发送测试结果
	mail_to = "403208371@qq.com"
	mail.sendreport(mail_to)

