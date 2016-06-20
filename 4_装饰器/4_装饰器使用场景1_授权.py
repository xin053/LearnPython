#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 4_装饰器使用场景1_授权.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-19 09:44:26
    License: Apache License 2.0
    Description: 装饰器常用的场景之一就是授权，例如，用装饰器将一个业务逻辑函数赋予授权功能，达到了授权与业务
                 功能代码的分离。
    Example:
    ------------------------------------------------------------------------------------------------
"""


from functools import wraps

class Request:
    """
    regard as a http request
    """
    authorization = False

def authenticate():
    """
    turn a page ask for authorization
    """
    print("turn a page ask for authorization")
    print("authorization comfirmed")

def requires_auth(service_func):
    """
    decorate a function to have a authorization process
    """
    @wraps(service_func)
    def decorated(*args, **kwargs):
        """
        if not authorized,turn to a page ask for authorization
        """
        auth = request.authorization
        if not auth:
            authenticate()
        return service_func(*args, **kwargs) # call the function,not return the function
    return decorated

@requires_auth
def pay_function():
    """
    a function that do some payment work
    """
    print("pay something succeed")

if __name__ == '__main__':
    print("when authorization is False:")
    request = Request()
    pay_function()
    print("================================")
    print("when authorization is True:")
    request.authorization = True
    pay_function()
