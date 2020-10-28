# -*- coding: utf-8 -*-
# @Time    : 2020/10/25 12:41
# @Author  : xiaojing.guo
# @Description:浏览器复用
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestBrowserMultiplexe():
#使用options进行浏览器的复用，首先需要在dos里边输入命令调取chrome并打开企业微信链接并手动扫码登录成功
#然后通过option实现浏览器复用
    def setup_method(self,method):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def teardown_method(self,method):
        self.driver.quit()
    def test_weixin(self):
        self.driver.find_element_by_id("menu_contacts").click()
