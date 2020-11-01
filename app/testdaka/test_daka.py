# -*- coding: utf-8 -*-
# @Time    : 2020/11/1 13:19
# @Author  : xiaojing.guo
# @Description:微信打卡功能

# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class Test_daka:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "127.0.0.1:7555"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.WwMainActivity"
        caps["noReset"] = "True"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def test_daka(self):
        # 找到工作台进行点击
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 滚动页面直到找到元素打卡并进行点击，代码最好复制，自己敲容易报错
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()
        # 通过setting方法减少等待时间
        self.driver.update_settings({"waitForIdleTimeout": 0})
        # 切换到外出打卡tab
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        # 查询到包含次外出的元素并点击
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        # sleep(3)
        # 断言该页面的xml包含外出打卡成功
        # assert "外出打卡成功" in self.driver.page_source
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in self.driver.page_source)

    def teardown(self):
        self.driver.quit()
