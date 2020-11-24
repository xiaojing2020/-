# -*- coding: utf-8 -*-
# @Time    : 2020/11/11 19:43
# @Author  : xiaojing.guo
# @Description:基础配置信息


from appium.webdriver import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from appium import webdriver


class BasePage222:
    #封装一个黑名单，用于处理比如弹窗一些没必要的弹窗登录后点击左上角的删除按钮
    _black_list = [(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    #只能放到类变量中，做全局变量，放到find会重置,加_表示是隐藏的不想被.的时候隐出来
    _erro_num = 0
    _max_num = 3
    def __init__(self,driver: WebDriver = None):
        if driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".common.MainActivity"
            # 保留缓存，比如登录状态
            caps["noReset"] = "True"
            # 不停止应用，直接运行测试用例,所以每次执行完记得返回
            # caps["dontStopAppOnReset"] = "true"
            # 跳过初始化阶段
            #caps['skipDeviceInitialization'] = 'true'
            # 跳过server安装
            #caps['skipServerInstallation'] = 'true'
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver = driver

    #对find方法进行封装
    def find(self,by,locator=None):
        #因为有时候黑名单是一个元祖，这时候就要解包就传入两个函数，所以会存在locator为none的情况
        try:
            if locator is None:
                result = self.driver.find_element(*by)
            else:
                result = self.driver.find_element(by,locator)
            #找到黑名单进行关闭后重新调取find，这时候需要重置
            self._erro_num = 0
            return result
        except Exception as e:
            #如果页面没有找到元素错误的数大于设置的超过最大数值的话就抛出异常，否则就是加1
            if self._erro_num > self._max_num:
                raise e
            self._erro_num +=1
            for black_ele in self._black_list:
                #这里注意find_elements要写s
                ele = self.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    ele[0].click()
                    return self.find(by,locator)
                raise e
