#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 1_generators_生成器.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-16 00:22:28
    License: Apache License 2.0
    Description: 斐波那契数列演示生成器
    Example:
    ------------------------------------------------------------------------------------------------
"""


def fibon(n):
    """
    fibon
    """
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    for i in fibon(100):
        print(i)
