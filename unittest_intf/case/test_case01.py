import pytest

from pytest_intf.api_keys.api_keys import ApiKey

class Test_ApiCase():
    def test_01(self):
        # 初始化工具类
        ak = ApiKey()
        #定义接口URL
        url = 'https://api.convertlab.com/v2/oauth2/token?grant_type=client_credentials'
        data = {
            "app_id": "cl004c1891f8ea20f",
            "secret": "ec290077c5e89fe5498289a1f2ab754267c1a1bc"
        }

        res = ak.post(url, data=data)
        print(res.text)
        #获取响应中的文本
        msg = ak.get_text(res.text, 'access_token')
        print(msg)
        assert msg

if __name__ == '__main__':
    pytest.main(['-s','test_case01.py'])

