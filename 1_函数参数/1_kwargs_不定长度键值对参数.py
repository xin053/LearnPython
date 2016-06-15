#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 1_kwargs_不定长度键值对参数.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-15 23:42:41
    License: Apache License 2.0
    Description: **kwargs参数的使用
    Example:
    ------------------------------------------------------------------------------------------------
"""


def greet_me(**kwargs):
    """
    the usage of **kwargs
    """
    for key, value in kwargs.items():
        print("{0} == {1}".format(key, value))

if __name__ == '__main__':
    greet_me(name="zzx")


