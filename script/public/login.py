# -*- coding:UTF-8 -*-
from selenium import webdriver
import time
def login(self):
	driver = self.driver
	time.sleep(1)
	driver.find_element_by_class_name("head_wrapper").find_element_by_xpath("/html/body/div[3]/div[1]/div/div[3]/a[7]").click()
	time.sleep(1)
	driver.find_element_by_id("passport-login-pop").find_element_by_id("TANGRAM__PSP_8__userName").clear()	
	time.sleep(1)
	driver.find_element_by_id("TANGRAM__PSP_2__foreground").find_element_by_xpath("/html/body/div[6]/div[2]/div[2]/div/div/div/div/div/div[1]/form/p[5]/input").send_keys(u"不调皮的杏仁")
	time.sleep(1)
	driver.find_element_by_id("TANGRAM__PSP_2__foreground").find_element_by_xpath("id('TANGRAM__PSP_8__password')").send_keys("wangxu978412")
	time.sleep(1)
	driver.find_element_by_id("TANGRAM__PSP_2__foreground").find_element_by_xpath("id('TANGRAM__PSP_8__submit')").click()
