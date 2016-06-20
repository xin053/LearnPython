#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 5_装饰器使用场景2_日志.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-19 10:20:41
    License: Apache License 2.0
    Description: 装饰器常用的场景之二就是日志，在使用函数之前输出日志信息
    Example:
    ------------------------------------------------------------------------------------------------
"""


from functools import wraps

def logit(func):
    """
    do some log
    """
    @wraps(func)
    def with_logging(*args, **kwargs):
        """
        do some log
        """
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logit
def addition_func(number):
    """Do some math."""
    return number + number


if __name__ == '__main__':
    result = addition_func(4)
    print(result)
    # Output: addition_func was called
    #         8
