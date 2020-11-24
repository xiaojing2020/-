# -*- coding: utf-8 -*-
# @Time    : 2020/11/12 19:01
# @Author  : xiaojing.guo
# @Description:首页配置 通过首页进入到行情-市场
import yaml
from selenium.webdriver.common.by import By

from blacklist.basepage import BasePage
from blacklist.hangqing import HangQing
from blacklist.market import Market

#继承basePage把上边的driver给继承过来
class Main(BasePage):
    def go_hangqing(self):
        #进一步进行封装，把下边的都写入yaml文件中
        # self.find(By.XPATH,"//*[@resource-id=	'com.xueqiu.android:id/post_status']").click()
        # self.find(By.XPATH,"//*[@resource-id='android:id/tabs']//*[@text ='行情']").click()
        #下边是不通过封装方法，直接读取自己的yaml文件
        # with open("./hangqing.yaml",encoding="utf-8")as f:
        #     data = yaml.load(f)
        #     steps = data["go_hangqing"]
        # for step in steps:
        #     if "click" == step["action"]:
        #         #step["by"]取得是value值"xpath"，而By源码里边By.XPATH = "xpath"，所以进行引用
        #         self.find(step["by"],step["locator"]).click()
        #         print(step["by"],step["locator"])
        self.parse_yaml("./hangqing.yaml","go_hangqing")
        #记得要传递driver到下边的类
        return HangQing(self.driver)
