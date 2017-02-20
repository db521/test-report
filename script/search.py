# -*- coding:UTF-8 -*-
import unittest,sys,time
sys.path.append("E:\\worksp\\function_library")
from function_library import excel
from  selenium import webdriver
class search(unittest.TestCase):
	
	
	def setUp(self):
		self.driver = webdriver.Firefox()

		
	def test_search(self):
		
		url = 
		#读取用例 
		data_path = "E:\\worksp\\data\\search.xls"
		search_Range = excel.readColValue(data_path,"testdata",1)#获取检索范围
		search_yuzhong = excel.readColValue(data_path,"testdata",2) #获取检索语种
		search_shezhi = excel.readColValue(data_path,"testdata",3)#获取检索设置
		search_word = excel.readColValue(data_path,"testdata",4) #获取检索词
		res_word = excel.readColValue(data_path,"testdata",5) #获取目标检索式
		res_num = excel.readColValue(data_path,"testdata",6) #获取期望检索结果
		browser = self.driver
		browser.get(url)
		#定位检索输入框
		webEdit = browser.find_element_by_id("ac_keybox_0")
		#定位检索按钮
		webButton = browser.find_element_by_id("btnSearch")
		#定位检索语种
		webLists_xpath = "id('btnLanguage')/option"#获取全部语种XPATH
		#定位检索范围 主题、学科、机构、人物、基金等XPATH
		webRaidoGroup_xpath = "id('con_one_1')/input"
		#定位检索设置XPATH
		webCheckBoxs_xpath = "id('shezhi')/input"
		
		for i in range(1,len(search_Range)):
			#判断语种设置的XPATH
			if search_yuzhong[i] == "全部":
				search_yuzhong_xpath = webLists_xpath + "[1]"

			elif search_yuzhong[i] == "中文":
				search_yuzhong_xpath = webLists_xpath + "[2]"

			else:
				search_yuzhong_xpath = webLists_xpath + "[3]"
			time.sleep(2)
			browser.find_element_by_xpath(search_yuzhong_xpath).click()

			#设置检索范围
			if search_Range[i] == "全部":
				webRaido_xpath = webRaidoGroup_xpath + "[1]"
			elif search_Range[i] == "主题":
				webRaido_xpath = webRaidoGroup_xpath + "[2]"
			elif search_Range[i] == "学科":
				webRaido_xpath = webRaidoGroup_xpath + "[3]"
			elif search_Range[i] == "机构":
				webRaido_xpath = webRaidoGroup_xpath + "[4]"
			elif search_Range[i] == "人物":
				webRaido_xpath = webRaidoGroup_xpath + "[5]"
			else :
				webRaido_xpath = webRaidoGroup_xpath + "[6]"
			time.sleep(2)
			browser.find_element_by_xpath(webRaido_xpath).click()

			#设置检索设置
			if search_shezhi[i] == "全部":
				search_shezhi_xpath = webCheckBoxs_xpath + "[1]"

			elif search_shezhi[i] == "中文":
				search_shezhi_xpath = webCheckBoxs_xpath + "[2]"

			else:
				search_shezhi_xpath = webCheckBoxs_xpath + "[3]"
			time.sleep(2)
			browser.find_element_by_xpath(search_shezhi_xpath).click()
			#输入检索词

			time.sleep(2)
			webEdit = browser.find_element_by_id("ac_keybox_0")
			webEdit.send_keys(search_word[i])
			#点击检索按钮
			time.sleep(2)
			webButton = browser.find_element_by_id("btnSearch")
			webButton.click()

			browser.get(url)

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()
