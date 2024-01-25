#!/usr/bin/python3
# --*-- coding: utf-8 --*--
# @Author: chen li
# @Time: 2024/1/25 17:50
# @File: main_run.py.py

import os

import pytest


def run():
    #指定执行文件
    #pytest.main(['-s', '-q', './testcase/testcase01.py', '--clean-alluredir', '--alluredir=reports/allureresults'])
    #os.system(r"allure generate -c -o allure-report")
    #os.system('allure serve result')
    pytest.main(['./testcase/testcase01.py', '--alluredir', './result'])
    os.system('allure generate ./result -o ./report --clean')


if __name__ == '__main__':
    run()

