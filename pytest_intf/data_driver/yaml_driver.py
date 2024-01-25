#!/usr/bin/python3
# --*-- coding: utf-8 --*--
# @Author: chen li
# @Time: 2024/1/25 17:30
# @File: yaml_driver.py
#!/usr/bin/python3
# --*-- coding: utf-8 --*--
# @Author: chen li
# @Time: 2024/1/23 10:43 上午
# @File: yaml_driver.py

import yaml


def load_yaml(path):
    file = open(path, 'r', encoding='utf-8')
    data = yaml.load(file, Loader=yaml.FullLoader)
    return data
