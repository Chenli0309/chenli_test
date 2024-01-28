
#!/usr/bin/python3
# --*-- coding: utf-8 --*--
# @Author: chen li
# @Time: 2024/1/25 17:29
# @File: testcase01.py
# pytest增加allure测试报告内容
import json
import allure
import jsonpath
import pytest
import os
from pytest_intf_logic.api_key.api_key import ApiKey
from pytest_intf_logic.data_driver import yaml_driver
#from pytest_intf.params.allParams import *


@allure.epic("接口测试")
class ApiCase:

    def login(self, UserData):
        #动态获取参数化生成标题
        allure.dynamic.title(UserData['title'])
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
        with allure.step("校验响应结果"):
            msg = ak.get_text(res.text, 'expires_in')
            print(msg)
            assert msg == 7200


    def create_customer01(self, token_fix):
        # 初始化工具类，token
        ak,token = token_fix
        # 创建客户
        with allure.step("创建客户接口"):
            #URL 是全局变量，在params模块中
            #url = URL + 'v2/customers'
            url = 'https://api.convertlab.com/v2/customers'
            params = {
                "access_token": token,
                "forceUpdate": 'false'
            }

            data ={"customer": {
                    "name": "convertlab",
                    "gender": 2,
                    "mobile": "18356348977",
                    "email": "li.wang@163.com",
                    "birthday": "2000-11-19",
                    "wechat": "test432956",
                    "nickName": "格",
                    "country": "中国",
                    "province": "陕西",
                    "city": "西安",
                    "county": "小店区",
                    "homeAddress": "爱国路313号",
                    "officeAddress": "耶里路",
                    "qq": "1466504230",
                    "stage": "Subscriber",
                    "dateJoin": "2020-06-01T12:12:12Z",
                    "source": "微博",
                    "contentName": "XX宣传转发",
                    "attr1": "广告"
                  },
                  "identity": {
                    "type": "mobile",
                    "value": "18092157726",
                    "name": "手机号"
                  }
                }
            res1 = ak.post(url=url, data=json.dumps(data), params=params)
            #print(res1.text)
            result = json.loads(res1.text)
            #print(result)
            value = jsonpath.jsonpath(result, '$..{0}'.format('id'))
            print(value[0])
        with allure.step("校验响应结果"):
            assert value[0] > 0
        return value


    def search_customer02(self, token_fix):
        # 初始化工具类
        ak, token = token_fix
        with allure.step("获取创建客户接口获取客户ID"):
            value = self.create_customer01(token_fix)
        # 查询客户
        with allure.step("查询客户接口"):
            #url = URL +'v2/customers'
            url = 'https://api.convertlab.com/v2/customers'
            userid = value[0]
            data = {
                "access_token": token,
                "id": userid
            }
            res1 = ak.get(url=url, params=data)
            # print(res1.text)
            result = json.loads(res1.text)
            # print(result)
            value = jsonpath.jsonpath(result, '$..{0}'.format('id'))
            #print(value[0])
        with allure.step("校验响应结果"):
            assert value[0] == userid





if __name__ == '__main__':
    # pytest.main(['-s', '-q', 'testcase01.py',  '--alluredir=allure-results'])
    # os.system(r"allure generate -c -o allure-report")
    # os.system('allure serve result')
    pytest.main(['./testcase/testcase01.py', '--alluredir', './result1'])
    os.system('allure generate ./result -o ./report1 --clean')
