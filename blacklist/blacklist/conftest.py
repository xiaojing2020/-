# -*- coding: utf-8 -*-
# @Time    : 2020/11/18 16:21
# @Author  : xiaojing.guo
# @Description:封装录屏的方法
# import os
# import signal
# import subprocess
#
# import allure
# import pytest
# #autouse表示在用例中自动调用
# @pytest.fixture(scope="module",autouse=True)
# def record_vedio():
#     command = "scrcpy --record tmp.mp4"
#     #使用cmd命令，固定格式
#     p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr= subprocess.STDOUT)
#     print(p)
#     yield
#     #结束录制
#     os.kill(p.pid,signal.CTRL_C_EVENT)
