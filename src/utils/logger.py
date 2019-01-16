# -*- coding: utf-8 -*-

import logging


class AppLogger:

    def __init__(self, filepath):
        # 获取log的一个实例:可以通过增加不同的handler来丰富log实例的特性
        self.logger = logging.getLogger()
        # 指定了Log的输出端是文件，通过传入文件路劲来指定输出文件
        handler = logging.FileHandler(filepath)
        # 指定了FileHandler的输出格式:format的关键字,例如asctime，levelname
        formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        # 设置优先级：Logging模块定义了5种log信息的优先级
        # 优先级关系：DEBUG < INFO < WARNING < ERROR < CRITCAL
        self.logger.setLevel(logging.NOTSET)

    def debug(self, msg):
        self.logger.debug(self, msg)

    def info(self, msg):
        self.logger.info(self, msg)

    def warn(self, msg):
        self.logger.warning(self, msg)

    def error(self, msg):
        self.logger.error(self, msg)