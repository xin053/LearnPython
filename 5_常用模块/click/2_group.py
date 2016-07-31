#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Copyright©2016.All rights reserved by xin053.
    ------------------------------------------------------------------------------------------------
    FileName: 2_group.py
    Author: xin053
    Version: 1.0
    Time: 2016-07-30 16:25:38
    License: Apache License 2.0
    Description: 嵌套命令
    Example:
    ------------------------------------------------------------------------------------------------
"""


import click

@click.group()
def cli():
    click.echo('Hello world')

@cli.command()
def initdb():
    click.echo('Initialized the database')

@cli.command()
def dropdb():
    click.echo('Dropped the database')

if __name__ == '__main__':
    cli()

# F:\cookies\python\learnPython\5_常用模块\click>python 2_group.py --help
# Usage: 2_group.py [OPTIONS] COMMAND [ARGS]...

# Options:
#   --help  Show this message and exit.

# Commands:
#   dropdb
#   initdb
# F:\cookies\python\learnPython\5_常用模块\click>python 2_group.py initdb
# Hello world
# Initialized the database

# F:\cookies\python\learnPython\5_常用模块\click>python 2_group.py dropdb
# Hello world
# Dropped the database
