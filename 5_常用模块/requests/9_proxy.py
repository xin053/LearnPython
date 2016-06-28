#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 9_proxy.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-28 20:42:00
    License: Apache License 2.0
    Description: 使用代理
    Example:
    ------------------------------------------------------------------------------------------------
"""


import requests

if __name__ == '__main__':
    proxies = {
        'http': 'http://127.0.0.1:1080',
        'https': 'http://127.0.0.1:1080'
    }

    r = requests.get('https://www.google.com',proxies=proxies)
    print(r.status_code)
