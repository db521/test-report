# -*- coding:UTF-8 -*-
import time,smtplib,os 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

#定义发送邮件
def sendmail(file_new,mail_to):
	#定义发送邮箱
	mail_from = 'wolong35@126.com'
	#定义收件箱
	#mail_to = 'wangx@wanfangdata.com'
	#定义正文
	f = open(file_new,'rb')
	mail_body = f.read()
	f.close()
	msg = MIMEText(mail_body,_subtype = 'html',_charset = 'UTF-8')
	#定义发送标题
	msg['Subject'] = u"测试报告"
	#定义发送时间
	msg['date'] = time.strftime('%a,%d %b %Y %H: %M: %S %z')
	smtp = smtplib.SMTP()

	smtp.connect('smtp.126.com')
	smtp.login('wolong35@126.com', 'wangxu978412')
	smtp.sendmail(mail_from,mail_to,msg.as_string())

	smtp.quit()

	print ('email is send out !')

def sendreport(mail_to):
	result_dir = 'E:\\worksp\\report'
	lists = os.listdir(result_dir)
	lists.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not
os.path.isdir(result_dir+"\\"+fn) else 0)
	
	file_new = os.path.join(result_dir,lists[-2])
	print (file_new)
	sendmail(file_new,mail_to)