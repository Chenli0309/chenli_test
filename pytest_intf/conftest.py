#!/usr/bin/python3
# --*-- coding: utf-8 --*--
# @Author: chen li
# @Time: 2024/1/25 19:12
# @File: conftest.py
import os
import sys

import allure
import pytest

from pytest_intf.api_key.api_key import ApiKey

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '')))


# 项目级fix，整个项目只初始化一次

@pytest.fixture(scope='session', autouse=True)
def token_fix():
    # 初始化工具类
    ak = ApiKey()
    with allure.step("发送获取token请求，生成token,整个项目只生成一次"):
        # 定义接口URL
        url = 'https://api.convertlab.com/v2/oauth2/token?grant_type=client_credentials'
        data = {
            "app_id": "cl004c1891f8ea20f",
            "secret": "ec290077c5e89fe5498289a1f2ab754267c1a1bc"
        }
        # 获取响应中的文本
        res = ak.post(url, data=data)
        token = ak.get_text(res.text,'access_token')
        print(token)
        return ak, token

