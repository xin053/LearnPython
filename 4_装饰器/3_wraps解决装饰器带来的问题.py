#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 3_wrap解决装饰器带来的问题.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-19 09:32:20
    License: Apache License 2.0
    Description: 使用装饰器后，如果访问函数的名称，注释文档，参数列表，将会得到装饰器底层那个函数的信息，为
                 了得到原本函数的信息，可以使用@wraps注解，因为该注解接受一个函数来进行装饰，并加入了复制函
                 数名称、注释文档、参数列表等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性。
    Example:
    ------------------------------------------------------------------------------------------------
"""

from functools import wraps

def a_new_decorator(a_func):
    """
    decorator function
    """
    @wraps(a_func)
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
    print(a_function_requiring_decoration.__name__)
    # Output: a_function_requiring_decoration
