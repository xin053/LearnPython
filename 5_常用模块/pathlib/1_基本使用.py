#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 1_基本使用.py
    Author: xin053
    Version: 1.0
    Time: 2016-07-03 19:42:41
    License: Apache License 2.0
    Description: pathlib基本使用
    Example:
    ------------------------------------------------------------------------------------------------
"""


import pathlib

if __name__ == '__main__':
    
    p = pathlib.Path('.')
    all_dir = [x for x in p.iterdir() if x.is_dir()]
    print(all_dir)
    # output: [WindowsPath('.git'), WindowsPath('.idea'), WindowsPath('.vscode'), 
    #         WindowsPath('1_函数参数'), WindowsPath('2_生成器'), WindowsPath('3_常用函数'), 
    #         WindowsPath('4_装饰器), WindowsPath('5_常用模块')]
    # 在linux环境下，上述的WindowsPath都会变为PosixPath

    # list all python files
    pyfiles = list(p.glob('**/*.py'))
    print(pyfiles)

    # link the path
    p = pathlib.Path(r'F:\cookies\python')
    q = p / 'learnPython'
    print(q)
    # output: F:\cookies\python\learnPython

    # query some path properties
    print(q.exists())
    print(q.is_dir())

    # Opening a file
    q = q / "hello_world.py"
    with q.open() as f:
        print(f.readline())
