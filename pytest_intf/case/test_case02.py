import pytest

from pytest_intf.api_keys.api_keys import ApiKey
from pytest_intf.data_driver import yaml_driver


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
    pytest.main(['-s', 'test_case02.py'])
