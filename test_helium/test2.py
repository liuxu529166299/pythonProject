# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @File     :test2
# @Date     :2022-08-11 14:59
# @Author   :刘旭
-------------------------------------------------
"""
from helium import *
from options import Options

options = Options().conf_option()
driver=start_chrome('https://www.baidu.com/',options=options)
write('测试',S('.s_ipt'))
click(S('#su'))
kill_browser()


