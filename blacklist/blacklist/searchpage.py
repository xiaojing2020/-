# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 14:18
# @Author  : xiaojing.guo
# @Description:进入到搜索页
from selenium.webdriver.common.by import By

from blacklist.basepage import BasePage


class Search(BasePage):
    def search_page(self):
        #self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/search_input_text']").send_keys("alibaba")
        self.parse_yaml("./search_Page.yaml","search_page")
