#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 1_基本使用.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-20 14:48:30
    License: Apache License 2.0
    Description: requests模块基本使用
    Example:
    ------------------------------------------------------------------------------------------------
"""


import requests

if __name__ == '__main__':
    # pass the url params as a dict
    payload = {'key1': 'value1', 'key2': 'value2'}

    # use GET method to send the HTTP request,want to use POST method? then use requests.post()
    r = requests.get('https://httpbin.org/get', params=payload)

    # get the whole url
    print(r.url)
    # output:   https://httpbin.org/get?key2=value2&key1=value1

    # when a key has several values
    payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
    r = requests.get('https://httpbin.org/get', params=payload)
    print(r.url)
    # output:   https://httpbin.org/get?key2=value2&key2=value3&key1=value1

    # if server return the content in JSON format,you can use json() to decode it
    print(r.json())

    # then,let's test a POST method
    payload = {'key1': 'value1', 'key2': 'value2'}
    r = requests.post("http://httpbin.org/post", data=payload)
    print(r.url)
    # output:   http://httpbin.org/post

    print(r.text)

    # then,send the params in json format
    payload = {'some': 'data'}
    r = requests.post("http://httpbin.org/post", json=payload)
    print(r.text)
