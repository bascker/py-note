# -*- coding: utf-8 -*-

from src.utils.logger import AppLogger

if __name__ == '__main__':
    LOGGER = AppLogger("a.log")
    LOGGER.info("aaa")