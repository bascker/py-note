#!/usr/bin/python
# -*- coding=utf-8 -*-
'''
使用 argparse 模块进行脚本参数解析
'''

from argparse import ArgumentParser
import os

def main():
    parse = ArgumentParser(description="python执行shell脚本")
    parse.add_argument("-c", "--cmd", required=False, default="echo run shell", help="shell 命令")
    args = parse.parse_args()

    cmd = args.cmd
    os.system(cmd)


if __name__ == '__main__':
    main()