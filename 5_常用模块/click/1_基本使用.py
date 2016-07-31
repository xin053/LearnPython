#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 1_基本使用.py
    Author: xin053
    Version: 1.0
    Time: 2016-07-19 14:20:08
    License: Apache License 2.0
    Description: click模块基本使用
    Example:
    ------------------------------------------------------------------------------------------------
"""


import click

@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)

if __name__ == '__main__':
    hello()

# to use this,you have to open your console,and type:python 1_基本使用.py [OPTIONS]
# for example:
# my environment:win10 x64
#
# F:\cookies\python\learnPython\5_常用模块\click>python 1_基本使用.py
# Your name: zzx
# Hello zzx!

# F:\cookies\python\learnPython\5_常用模块\click>python 1_基本使用.py --help
# Usage: 1_基本使用.py [OPTIONS]
# 
#   Simple program that greets NAME for a total of COUNT times.
#
# Options:
#   --count INTEGER  Number of greetings.
#   --name TEXT      The person to greet.
#   --help           Show this message and exit.