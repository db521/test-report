# -*- coding:UTF-8 -*-
from  selenium import webdriver
import unittest,sys,time
sys.path.append("E:\\worksp\\test_case\\public")

from public import login


class baidu(unittest.TestCase):
	
	def setUp(self):
		self.driver = webdriver.Firefox()
		
	def test_baidu_search(self):
		driver = self.driver
		driver.get("http://www.baidu.com/")
		login.login(self)
		driver.find_element_by_id('kw').send_keys('test')
		time.sleep(2)
		driver.find_element_by_id('su').click()

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":

	unittest.main()
	'''
	#构造测试集
	suite = unittest.TestSuite()
	suite.addTest(baidu('test_baidu'))
	#执行测试用例
	runner = unittest.TextTestRunner()
	runner.run(suite)

	'''