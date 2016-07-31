#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 3_argument.py
    Author: xin053
    Version: 1.0
    Time: 2016-07-30 16:55:42
    License: Apache License 2.0
    Description: 给命令增加参数
    Example:
    ------------------------------------------------------------------------------------------------
"""


import click

@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()

# F:\cookies\python\learnPython\5_常用模块\click>python 3_argument.py
# Usage: 3_argument.py [OPTIONS] NAME

# Error: Missing argument "name".

# F:\cookies\python\learnPython\5_常用模块\click>python 3_argument.py --help
# Usage: 3_argument.py [OPTIONS] NAME

# Options:
#   --count INTEGER  number of greetings
#   --help           Show this message and exit.

# F:\cookies\python\learnPython\5_常用模块\click>python 3_argument.py zzx
# Hello zzx!
