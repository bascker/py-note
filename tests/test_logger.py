# -*- coding: utf-8 -*-

from src.utils.logger import AppLogger

if __name__ == '__main__':
    LOGGER = AppLogger(name='mylog', filepath='file/my.log')
    LOGGER.debug("bbb")