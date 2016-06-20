#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 4_cookie.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-20 15:55:50
    License: Apache License 2.0
    Description: 获取cookie以及在请求中附加自定义cookie
    Example:
    ------------------------------------------------------------------------------------------------
"""


import requests

if __name__ == '__main__':
    r = requests.get('https://httpbin.org/get')

    # get the cookies that the server set
    print(r.cookies)

    cookies = dict(user='xin053')

    # send a GET request with custom cookie
    r = requests.get('https://httpbin.org/get', cookies=cookies)
    print(r.text)
