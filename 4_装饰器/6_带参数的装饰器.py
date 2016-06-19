#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 6_带参数的装饰器.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-19 10:54:24
    License: Apache License 2.0
    Description: 带参数的装饰器在外面又嵌套一层
    Example:
    ------------------------------------------------------------------------------------------------
"""


from functools import wraps

def logit(logfile='out.log'):
    """a decorator that has parameter"""
    def logging_decorator(func):
        """decorate the function to have log feature"""
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            """log"""
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    """myfunc1"""
    print("call myfunc1()")


@logit(logfile='func2.log')
def myfunc2():
    """myfunc2"""
    print("call myfunc2()")



if __name__ == '__main__':
    myfunc1()
    # Output: myfunc1 was called
    # 现在一个叫做 out.log 的文件出现了，里面的内容就是上面的字符串
    myfunc2()
    # Output: myfunc2 was called
    # 现在一个叫做 func2.log 的文件出现了，里面的内容就是上面的字符串
