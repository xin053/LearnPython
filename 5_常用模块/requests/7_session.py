#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 7_session.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-20 17:12:52
    License: Apache License 2.0
    Description: session能对一些参数，cookies等进行持久化，也就是每次http请求都会带上
    Example:
    ------------------------------------------------------------------------------------------------
"""


import requests

if __name__ == '__main__':
    # you can also use 's = requests.Session()',but I strongly recommend that using 'with'
    with requests.Session() as s:
        s.get('http://httpbin.org/cookies/set/user/xin053')
        r = s.get('http://httpbin.org/cookies')
        print(r.text)
        # output: {
        #             "cookies": {
        #                 "user": "xin053"
        #             }
        #         }

        # session object will add the cookies information automatically
        r = s.get('http://httpbin.org/get')
        print(r.text)
        # output: {
        #             "args": {}, 
        #             "headers": {
        #                 "Accept": "*/*", 
        #                 "Accept-Encoding": "gzip, deflate", 
        #                 "Cookie": "user=xin053",     
        #                 "Host": "httpbin.org", 
        #                 "User-Agent": "python-requests/2.10.0"
        #             }, 
        #             "origin": "113.57.220.65", 
        #             "url": "http://httpbin.org/get"
        #         }

        # Sessions can also be used to provide default data to the request methods.
        # This is done by providing data to the properties on a Session object
        s.params.update({'userName': 'zzx'})
        s.headers.update({'test': 'true'})
        s.headers.update({'test1': 'false'})
        # Any dictionaries that you pass to a request method will be merged with the session-level values that are set.
        # The method-level parameters override session parameters.
        r = s.get('http://httpbin.org/get', params={'pass': '123456'}, headers={'test1': 'true'})
        print(r.text)
        # output: {
        #             "args": {
        #                 "pass": "123456", 
        #                 "userName": "zzx"
        #             }, 
        #             "headers": {
        #                 "Accept": "*/*", 
        #                 "Accept-Encoding": "gzip, deflate", 
        #                 "Host": "httpbin.org", 
        #                 "Test": "true", 
        #                 "Test1": "true", 
        #                 "User-Agent": "python-requests/2.10.0"
        #             }, 
        #             "origin": "113.57.220.65", 
        #             "url": "http://httpbin.org/get?userName=zzx&pass=123456"
        #         }

        # you can see that the request below send the 'userName' args,note the url
        r = s.get('http://httpbin.org/get')
        print(r.text)
        # output: {
        #             "args": {
        #                 "userName": "zzx"
        #             }, 
        #             "headers": {
        #                 "Accept": "*/*", 
        #                 "Accept-Encoding": "gzip, deflate", 
        #                 "Host": "httpbin.org", 
        #                 "Test": "true", 
        #                 "Test1": "false", 
        #                 "User-Agent": "python-requests/2.10.0"
        #             }, 
        #             "origin": "113.57.220.65", 
        #             "url": "http://httpbin.org/get?userName=zzx"
        #         }
