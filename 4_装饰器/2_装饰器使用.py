#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 2_装饰器使用.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-19 09:26:23
    License: Apache License 2.0
    Description: 装饰器使用：通过注解
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

@a_new_decorator
def a_function_requiring_decoration():
    """
    the function that will be decorated
    """
    print("I am the function which needs some decoration to remove my foul smell")

if __name__ == '__main__':
    a_function_requiring_decoration()
    #outputs: I am doing some boring work before executing a_func()
    #         I am the function which needs some decoration to remove my foul smell
    #         I am doing some boring work after executing a_func()

    #the @a_new_decorator is just a short way of saying:
    #a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
