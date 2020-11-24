# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 13:52
# @Author  : xiaojing.guo
# @Description:打开行情页点击市场进入到市场页
from selenium.webdriver.common.by import By

from blacklist.basepage import BasePage
from blacklist.market import Market

#继承上边的类
class HangQing(BasePage):
    def go_market(self):
        #self.find(By.XPATH,"//*[(@resource-id='com.xueqiu.android:id/title_text')and contains(@text,'市场')]").click()
        self.parse_yaml("go_Maket.yaml", "go_market")
        return Market(self.driver)