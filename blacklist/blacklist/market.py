# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 19:41
# @Author  : xiaojing.guo
# @Description:点击右上角的搜索按钮进入到搜索页
from selenium.webdriver.common.by import By

from blacklist.basepage import BasePage
from blacklist.searchpage import Search


class Market(BasePage):
    def go_search(self):
        #self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        self.parse_yaml("go_Search.yaml", "go_search")
        return Search(self.driver)




