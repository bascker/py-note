# -*- coding: utf-8 -*-
'''
日志
'''
import logging
from logging import handlers


class AppLogger:
    '''
    日志记录器，支持输出到控制台 & 文件
    '''
    DEBUG = 0
    INFO = 1
    WARN = 2
    ERROR = 3
    CRITICAL = 4

    __level = {
        DEBUG: logging.DEBUG,
        INFO: logging.INFO,
        WARN: logging.WARNING,
        ERROR: logging.ERROR,
        CRITICAL: logging.CRITICAL
    }

    def __init__(self, name=None, level=None, filepath=None):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(self.__level.get(level, logging.DEBUG))

        if name is not None:
            fmt = logging.Formatter(
                '%(asctime)s %(threadName)s-%(thread)d %(name)s.%(funcName)s[line:%(lineno)d] %(levelname)s %(message)s')
        else:
            fmt = logging.Formatter(
                '%(asctime)s %(threadName)s-%(thread)d %(filename)s.%(funcName)s[line:%(lineno)d] %(levelname)s %(message)s')
        # 输出到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(fmt)
        self.logger.addHandler(stream_handler)

        if filepath is not None:
            # 按天打包日志文件
            file_handler = handlers.TimedRotatingFileHandler(filename=filepath, when='D', backupCount=3, encoding='utf-8')
            file_handler.setFormatter(fmt)
            self.logger.addHandler(file_handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)
