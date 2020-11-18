# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 19:01
# @Author  : xiaojing.guo
# @Description:首页配置 通过首页进入到行情-市场

from selenium.webdriver.common.by import By

from blacklist.basepage222 import BasePage
from blacklist.hangqing import HangQing
from blacklist.market import Market

#继承basePage把上边的driver给继承过来
class Main(BasePage):
    def go_hangqing(self):
        self.find(By.XPATH,"//*[@resource-id=	'com.xueqiu.android:id/post_status']").click()
        self.find(By.XPATH,"//*[@resource-id='android:id/tabs']//*[@text ='行情']").click()
        #记得要传递driver到下边的类
        return HangQing(self.driver)
