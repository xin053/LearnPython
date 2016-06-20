#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 2_自定义请求头.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-20 15:13:34
    License: Apache License 2.0
    Description: 自定义http请求头
    Example:
    ------------------------------------------------------------------------------------------------
"""


import requests

if __name__ == '__main__':
    # customize the HTTP header
    headers = {'user-agent' : 'iphone 6s'}
    r = requests.get('https://httpbin.org/get', headers=headers)
    print(r.text)
    # output  {
    #             "args": {}, 
    #             "headers": {
    #                 "Accept": "*/*", 
    #                 "Accept-Encoding": "gzip, deflate", 
    #                 "Host": "httpbin.org", 
    #                 "User-Agent": "iphone 6s"
    #             }, 
    #             "origin": "113.57.220.65", 
    #             "url": "https://httpbin.org/get"
    #         }

    # get the request header you just sent
    print(r.request.headers)

