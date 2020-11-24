# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 17:06
# @Author  : xiaojing.guo
# @Description:使用装饰器的方法对原有方法进行扩展
import allure




def handle_black(func):
    #使用wrapper进行加强一下
    def wrapper(*args, **kwargs):
        from blacklist.basepage import BasePage
        #可以理解成把调取的方法的第一个参数self传过来,basepage的一个实例
        isinstance : BasePage = args[0]
        try:
           result = func(*args,**kwargs)
           isinstance.erro_num = 0
           return  result
        except Exception as e:
            #对异常的黑名单进行截图处理
            isinstance.driver.save_screenshot("tmp.png")
            with open("tmp.png","rb")as f:
                content = f.read()
            allure.attach(content,attachment_type=allure.attachment_type.PNG)
            #如果页面没有找到元素错误的数大于设置的超过最大数值的话就抛出异常，否则就是加1
            if isinstance.erro_num > isinstance.max_num:
                raise e
            isinstance.erro_num +=1
            for black_ele in isinstance.black_list:
                #这里注意find_elements要写s
                ele = isinstance.driver.find_elements(*black_ele)
                if len(ele) > 0:
                    ele[0].click()
                    return wrapper(*args,**kwargs)
            raise e
    #注意这里千万不能写如果写了的话就不进行调用异常方法了()
    return wrapper




