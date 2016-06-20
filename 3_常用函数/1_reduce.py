#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 1_reduce.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-18 23:16:28
    License: Apache License 2.0
    Description: reduce函数使用
    Example:
    ------------------------------------------------------------------------------------------------
"""


from functools import reduce

if __name__ == '__main__':
    product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
    print(product)
