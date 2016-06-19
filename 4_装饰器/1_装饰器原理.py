#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 1_装饰器原理.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-19 09:18:41
    License: Apache License 2.0
    Description: 装饰器原理:传递函数，返回函数'
    Example:
    ------------------------------------------------------------------------------------------------
"""


def a_new_decorator(a_func):
    """
    decorator function
    """
    def wrap_the_function():
        """
        the actually returned function
        """
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrap_the_function

def a_function_requiring_decoration():
    """
    the function that will be decorated
    """
    print("I am the function which needs some decoration to remove my foul smell")


if __name__ == '__main__':
    a_function_requiring_decoration()
    #outputs: "I am the function which needs some decoration to remove my foul smell"

    a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
    #now a_function_requiring_decoration is wrapped by wrapTheFunction()

    a_function_requiring_decoration()
    #outputs:I am doing some boring work before executing a_func()
    #        I am the function which needs some decoration to remove my foul smell
    #        I am doing some boring work after executing a_func()


