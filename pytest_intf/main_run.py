#!/usr/bin/python3
# --*-- coding: utf-8 --*--
# @Author: chen li
# @Time: 2024/1/23 11:48 上午
# @File: main_run.py
import os

import pytest


def run():
    #指定执行文件
    pytest.main(['-v','./case/test_case03.py',
                 '--alluredir','./result','--clean-alluredir'])
    os.system('allure serve result')


if __name__ == '__main__':
    run()