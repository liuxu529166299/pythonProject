# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @File     :test1
# @Date     :2022-07-29 15:23
# @Author   :刘旭
-------------------------------------------------
"""

from helium import *
from time import sleep
from options import Options
from selenium import webdriver

loc='//*[@id="root"]/section/main/div[2]/div[3]/div/div/div[1]/div[1]/div/div/div/div/div/div/table/tbody/tr/td[5]/a'
loc1='/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]'
loc2='/html/body/div[2]/div/div[2]/div/div[2]/button/span/i/svg'
home_url = 'http://175.6.6.61:61507/workstation/#/login'
#帐号
login_name ='3870'
#密码
login_pwd='lx7890'
options = Options().conf_option()
driver = start_chrome(home_url,options=options)
write(login_name,TextField('请输入用户名'))
write(login_pwd,TextField('请输入密码'))
#click('//*[@id="root"]/div/div/div[2]/form/div[4]/div/div/span/button')ddddddddddddddddddd
click('登 录')
sleep(2)
click(S('.ant-modal-close-x'))
#el=driver.find_element_by_xpath(loc1)
#doubleclick(el)11111111
#doubleclick('内分泌门诊')
#click('已接诊')
#doubleclick('测试患者一')
#click('诊断')
#write('健康查体',TextField('查询诊断'))
#press(DOWN)
#press(ENTER)
#sleep(3)
#click(Button('一键下诊断',below='历史诊断'))
#driver.find_element_by_xpath(loc).click()
#click('确 定')
#refresh()
sleep(3)
#click('打 印')
#click('更多功能')
#sleep(5)
kill_browser()
