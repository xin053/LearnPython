#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 2_args_kwargs_传递参数.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-16 00:03:57
    License: Apache License 2.0
    Description: 使用*args **kwargs传递参数
    Example:
    ------------------------------------------------------------------------------------------------
"""


def test_args_kwargs(arg1, arg2, arg3):
    """
    a test function
    """
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

if __name__ == '__main__':
    args = ["one", 2, 3]
    test_args_kwargs(*args)

    args = ("two", 3, 5)
    test_args_kwargs(*args)

    kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
    test_args_kwargs(**kwargs)


