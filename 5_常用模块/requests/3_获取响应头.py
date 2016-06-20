#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 3_获取响应头.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-20 15:32:35
    License: Apache License 2.0
    Description: 获取http响应头
    Example:
    ------------------------------------------------------------------------------------------------
"""


import requests

if __name__ == '__main__':
    r = requests.get('http://httpbin.org/get')
    print(r.status_code)
    # output:    200

    print(r.status_code == requests.codes.ok)
    # output:    True

    # you can also use the return code to raise an exception
    bad_r = requests.get('http://httpbin.org/status/404')
    print(bad_r.status_code)
    # output:   404

    bad_r.raise_for_status()
    # output:   Traceback (most recent call last):
    #           File "f:\cookies\python\learnPython\5_常用模块\requests\3_获取响应头.py", line 33, in <module>
    #               bad_r.raise_for_status()
    #           File "D:\Python 3.5\lib\site-packages\requests\models.py", line 844, in raise_for_status
    #               raise HTTPError(http_error_msg, response=self)
    #           requests.exceptions.HTTPError: 404 Client Error: NOT FOUND for url: http://httpbin.org/status/404

    # and when the return code is 200,raise_for_status() will get None
    r = requests.get('http://httpbin.org/get')
    r.raise_for_status()
    # output:   None

    # get the HTTP response header
    print(r.headers)

    # you can get header information in any ways below,and you can also ignore the case
    print(r.headers['Content-Type'])
    print(r.headers.get('conTent-type'))
