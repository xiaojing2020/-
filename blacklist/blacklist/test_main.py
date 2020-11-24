# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 10:24
# @Author  : xiaojing.guo
# @Description:
from blacklist.mainpage import Main
# import sys
# import os
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(rootPath)

class TestMain:
    def test_main(self):
        main = Main().go_hangqing().go_market().go_search().search_page()

