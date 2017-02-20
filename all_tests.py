# -*- coding:UTF-8 -*-
import unittest,time,HTMLTestRunner,os,sys
sys.path.append("E:\\worksp\\function_library")
from function_library import mail

list_case_path = 'E:\\worksp\\test_case'

def creatsuitel():
	testunit = unittest.TestSuite()
	discover = unittest.defaultTestLoader.discover(
		list_case_path,
		pattern = '*.py',
		top_level_dir = None
		)

	for test_suite in discover:
		for test_case in test_suite:
			testunit.addTests(test_case)
			print test_case
	return testunit

alltestcasesname = creatsuitel()

now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))
filename = "E:\\worksp\\report\\"+now+"result.html"
fp = file(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(
	stream = fp,
	title = u"测试报告",
	description = u"用例执行结果"
	)

if __name__ == "__main__":
	#执行测试用例集
	runner.run(alltestcasesname)
	#发送测试结果
	mail_to = "wangx@wanfangdata.com.cn"
	mail.sendreport(mail_to)

