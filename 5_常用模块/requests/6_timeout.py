#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 6_timeout.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-20 16:03:53
    License: Apache License 2.0
    Description: 自定义timeout
    Example:
    ------------------------------------------------------------------------------------------------
"""


import requests

if __name__ == '__main__':
    requests.get('http://github.com', timeout=0.001)
    # output: Traceback (most recent call last):
    #         File "f:\cookies\python\learnPython\5_常用模块\requests\6_timeout.py", line 21, in <module>
    #             requests.get('http://github.com', timeout=0.001)
    #         File "D:\Python 3.5\lib\site-packages\requests\api.py", line 71, in get
    #             return request('get', url, params=params, **kwargs)
    #         File "D:\Python 3.5\lib\site-packages\requests\api.py", line 57, in request
    #             return session.request(method=method, url=url, **kwargs)
    #         File "D:\Python 3.5\lib\site-packages\requests\sessions.py", line 475, in request
    #             resp = self.send(prep, **send_kwargs)
    #         File "D:\Python 3.5\lib\site-packages\requests\sessions.py", line 585, in send
    #             r = adapter.send(request, **kwargs)
    #         File "D:\Python 3.5\lib\site-packages\requests\adapters.py", line 459, in send
    #             raise ConnectTimeout(e, request=request)
    #         requests.exceptions.ConnectTimeout: HTTPConnectionPool(host='github.com', port=80): 
    #         Max retries exceeded with url: / (Caused by ConnectTimeoutError(<requests.packages.urllib3.connection.HTTPConnection object 
    #         at 0x0000025D8AF77470>, 'Connection to github.com timed out. (connect timeout=0.001)'))