#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 5_请求重定向.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-20 16:03:53
    License: Apache License 2.0
    Description: http请求重定向，默认情况下，requests将所有的请求自动重定向，并把完成整个连接的所有请求放在
                 Response.history中，当然也可以手动关闭自动重定向
    Example: github的所有http连接都会重定向到https，也就是访问http://github.com时，
             会重定向到https://github.com
    ------------------------------------------------------------------------------------------------
"""


import requests

if __name__ == '__main__':
    # when redirection automatically
    r = requests.get('http://github.com')
    print(r.url)
    # output:    https://github.com/

    print(r.history)
    # output:   [<Response [301]>]

    # when turn off the redirection
    r = requests.get('http://github.com', allow_redirects=False)
    print(r.url)
    # output:    http://github.com/

    print(r.history)
    # output:   []
