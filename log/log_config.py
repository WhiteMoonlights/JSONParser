#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
@File    :   requests_complexes.requests_complexes.py
@Time    :   2021/5/11
@Author  :   yingjie
@Github :    https://github.com/WhiteMoonlights/API_Tester.git
@Contact :   ajie_jason@163.com
@Desc    :   请求方法集合
"""

import logging
import logging.handlers
import os
import time
import colorlog


class GetLogger:
    def __init__(self):
        logging.getLogger('chardet.charsetprober').setLevel(logging.INFO)
        self.logger = logging.getLogger("")
        self.logger.handlers.clear()
        # 设置输出的等级
        LEVELS = {'NOSET': logging.NOTSET,
                  'DEBUG': logging.DEBUG,
                  'INFO': logging.INFO,
                  'WARNING': logging.WARNING,
                  'ERROR': logging.ERROR,
                  'CRITICAL': logging.CRITICAL}
        # 设置日志输出颜色
        log_colors_config = {
            'DEBUG': 'white',
            'INFO': 'white',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }
        # 创建文件目录
        logs_dir = os.path.dirname(__file__)
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
            pass
        else:
            os.mkdir(logs_dir)
        # 修改log保存位置
        timestamp = time.strftime("%Y-%m-%d", time.localtime())
        logfilename = '%s.txt' % timestamp
        logfilepath = os.path.join(logs_dir, logfilename)
        rotatingFileHandler = logging.handlers.RotatingFileHandler(filename=logfilepath,
                                                                   maxBytes=1024 * 1024 * 50,
                                                                   backupCount=5,
                                                                   encoding="utf-8")
        # 设置输出格式
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        rotatingFileHandler.setFormatter(formatter)
        # 控制台句柄
        con_formatter = colorlog.ColoredFormatter(fmt='%(log_color)s[%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S', log_colors=log_colors_config)
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.INFO)
        self.console.setFormatter(con_formatter)
        # 添加内容到日志文件句柄中
        self.logger.addHandler(rotatingFileHandler)
        self.logger.addHandler(self.console)
        self.logger.setLevel(logging.DEBUG)

    def info(self, message):
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)


if __name__ == '__main__':
    GetLogger().info("开始输出日志")