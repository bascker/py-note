# -*- coding: utf-8 -*-
import os
import sys
# 用于引入自定义模块: 若当前目录查不到，则 import 模块从 sys.path 找
sys.path.append(os.getcwd())

from src.utils.applogger import AppLogger

if __name__ == '__main__':
    LOGGER = AppLogger(name='mylog', filepath=os.path.join(os.getcwd(), "test", "file", "my.log"))
    LOGGER.debug("test_applogger")
