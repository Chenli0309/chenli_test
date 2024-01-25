#pytest增加allure测试报告内容
import allure
import pytest
import os
from pytest_intf.api_keys.api_keys import ApiKey
from pytest_intf.data_driver import yaml_driver


@allure.story("获取token")
class Test_ApiCase():
    @pytest.mark.parametrize('UserData', yaml_driver.load_yaml('../data/appid.yaml'))
    def test_01(self,UserData):
        # 初始化工具类
        ak = ApiKey()
        # 定义接口URL
        url = 'https://api.convertlab.com/v2/oauth2/token?grant_type=client_credentials'
        data = {
            "app_id": UserData['user']['app_id'],
            "secret": UserData['user']['secret']
        }
        #print(UserData['user']['app_id'])
        res = ak.post(url, data=data)
        print(res.text)
        # 获取响应中的文本
        msg = ak.get_text(res.text, 'expires_in')
        print(msg)
        assert msg


if __name__ == '__main__':
    pytest.main(['-v', './case/test_case03.py',
                 '--alluredir', './result', '--clean-alluredir'])
    os.system('allure serve result')