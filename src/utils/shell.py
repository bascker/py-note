# -*- coding: utf-8 -*-

import os


def run(command):
    '''
    运行命令
    :param command: Shell 命令
    :return:
    '''
    if not command:
        print("command is null")

    return os.popen(command)