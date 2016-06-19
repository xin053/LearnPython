#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 7_类装饰器.py
    Author: xin053
    Version: 1.0
    Time: 2016-06-19 11:09:33
    License: Apache License 2.0
    Description: 类装饰器
    Example:
    ------------------------------------------------------------------------------------------------
"""


from functools import wraps

class Logit(object):
    """a log class"""
    def __init__(self, logfile='out.log'):
        self.logfile = logfile

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            """simplly add something to a log file"""
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile并写入
            with open(self.logfile, 'a') as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + '\n')
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)
        return wrapped_function

    def notify(self):
        """you can do other log method in this function"""
        # logit只打日志，不做别的
        pass

class EmailLogit(Logit):
    '''
    一个logit的实现版本，可以在函数调用时发送email给管理员
    '''
    def __init__(self, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(EmailLogit, self).__init__(*args, **kwargs)

    def notify(self):
        # 发送一封email到self.email
        # 这里就不做实现了
        pass


if __name__ == '__main__':
    @Logit()
    def myfunc1():
        """myfunc1"""
        print("call mufunc1()")

    @EmailLogit()
    def myfunc2():
        """myfunc2"""
        print("call mufunc2()")
