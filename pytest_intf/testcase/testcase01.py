#!/usr/bin/python3
# --*-- coding: utf-8 --*--
# @Author: chen li
# @Time: 2024/1/25 17:29
# @File: testcase01.py
# pytest增加allure测试报告内容
import allure
import pytest
import os
from pytest_intf.api_key.api_key import ApiKey
from pytest_intf.data_driver import yaml_driver


@allure.story("获取token")
class Test_ApiCase():
    @pytest.mark.parametrize('UserData', yaml_driver.load_yaml('./data/userinfo.yaml'))
    def test_01(self, UserData):
        # 初始化工具类
        ak = ApiKey()
        # 定义接口URL
        url = 'https://api.convertlab.com/v2/oauth2/token?grant_type=client_credentials'
        data = {
            "app_id": UserData['user']['app_id'],
            "secret": UserData['user']['secret']
        }
        # print(UserData['user']['app_id'])
        res = ak.post(url, data=data)
        print(res.text)
        # 获取响应中的文本
        msg = ak.get_text(res.text, 'expires_in')
        # print(msg)
        assert msg


if __name__ == '__main__':
    pytest.main(['-s', '-q', 'testcase01.py',  '--alluredir=allure-results'])
     #os.system(r"allure generate -c -o allure-report")
    os.system('allure serve result')
