import unittest

import ddt as ddt
from ddt import ddt, file_data
from pytest_intf.api_keys.api_keys import ApiKey


@ddt
class Test_ApiCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        # 初始化工具类
        cls.ak = ApiKey()

    @file_data('../data/appid.yaml')
    def test_01(self, user, msg):
        # 定义接口URL
        url = 'https://api.convertlab.com/v2/oauth2/token?grant_type=client_credentials'
        data = {
            "app_id": user['app_id'],
            "secret": user['secret']
        }
        # print(UserData['user']['app_id'])
        res = self.ak.post(url, data=data)
        print(res.text)
        # 获取响应中的文本
        msg1 = self.ak.get_text(res.text, 'expires_in')
        print(msg)
        self.assertEqual(msg1, msg)


if __name__ == '__main__':
    unittest.main()
