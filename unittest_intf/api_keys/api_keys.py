"""
这是接口关键字驱动类，用于接口自动化接口得是的关键字方法
主要用于实现长虹的关键字，并定义好参数即可
接口中常用的关键字：
get post put delete header
设置入参的默认值的时候，设置的参数必须放到最后

https://api.convertlab.com/v2/oauth2/token?grant_type=client_credentials
cl3@qq.com
app_id:cl004c1891f8ea20f
secret:ec290077c5e89fe5498289a1f2ab754267c1a1bc
grant_type:client_credentials

"""
import json
import jsonpath as jsonpath
import requests


class ApiKey:
    def get(self, url, params=None, **kwargs):
        # get方法封装
        return requests.get(url=url, params=params, **kwargs)

        # post方法封装

    def post(self, url, data=None, **kwargs):
        return requests.post(url=url,data=data, **kwargs)

    # 基于jsonpath获取数据的关键字，用于提取所需的内容
    def get_text(self, data, key):
        # jsonpath获取数据的表达式：成功则返回list,失败返回false
        json_data = json.loads(data)
        value = jsonpath.jsonpath(json_data, '$..{0}'.format(key))
        return value[0]


if __name__ == '__main__':
    ak = ApiKey()
    url = 'https://api.convertlab.com/v2/oauth2/token?grant_type=client_credentials'
    data = {
        "app_id": "cl004c1891f8ea20f",
        "secret": "ec290077c5e89fe5498289a1f2ab754267c1a1bc"
    }
    res = ak.post(url, data=data)
    print(res.text)

    #url = "http://httpbin.org/post"
    #d = {"key1": "value1", "key2": "value2"}
    #r = requests.post(url, data=d)  # requests.post() 中利用 data 属性
    #print(r.text)
    #res = requests.post(url=url, json=data)
    #print(res.text)
    #r = ak.post(url, data=data)  # requests.post() 中利用 data 属性

