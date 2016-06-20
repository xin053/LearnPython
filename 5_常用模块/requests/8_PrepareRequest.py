#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 8_PreareRequest.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-20 17:58:08
    License: Apache License 2.0
    Description: PreareRequest
    Example:
    ------------------------------------------------------------------------------------------------
"""


import requests

if __name__ == '__main__':
    s = requests.Session()
    req = requests.Request('GET', 'http://httpbin.org/get', data={'user': 'zzx'}, headers={'test': 'true'})
    prepped = s.prepare_request(req)
    # do something with prepped.body
    prepped.body = 'Seriously, send exactly these bytes.'
    # do something with prepped.headers
    prepped.headers['Keep-Dead'] = 'parrot'
    resp = s.send(prepped)

    print(resp.text)