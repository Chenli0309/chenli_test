#!/usr/bin/python3
# --*-- coding: utf-8 --*--
# @Author: chen li
# @Time: 2024/1/25 17:29
# @File: testcase01.py
# pytest增加allure测试报告内容
import allure
import pytest

from pytest_intf_logic.data_driver import yaml_driver
from pytest_intf_logic.logic.CustomerManageApi import ApiCase


class TestTree():
    # 初始化用例库
    action = ApiCase()
    @allure.feature("00,获取token")
    @allure.story('一般场景')
    @pytest.mark.parametrize('UserData',yaml_driver.load_yaml('./data/userinfo.yaml'))
    def test_case01(self,UserData):
        self.action.login(UserData)

    @allure.feature("00,创建客户")
    @allure.story("01.创建客户")
    @allure.title('创建新客户')
    def test_case02(self, token_fix):
        self.action.create_customer01(token_fix)

    @allure.story("02.查询客户")
    def test_case03(self, token_fix):
        self.action.search_customer01(token_fix)