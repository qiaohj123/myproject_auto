# -*- coding:utf-8 -*-
import logging
import time
import os


class Log:
    def __init__(self):
        self.log_path = 'D:\PycharmProjects\\untitled\\rbuildemp\\report\log'
        self.logname = os.path.join(self.log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s[line:%(lineno)d] - fuc:%(funcName)s- %(levelname)s: %(message)s')

    def __console(self, level, message):
        fh = logging.FileHandler(self.logname, 'a')  # 追加模式
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)































# def get_log():
#     logger = logging.getLogger()
#     logger.setLevel(logging.DEBUG)
#
#     ts = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
#     path = 'D:\PycharmProjects\\untitled\emp73\\report\log'
#
#     all_logpath = os.path.join(path, 'All_Logs')
#     error_logpath = os.path.join(path, 'Error_Logs')
#
#     all_logname = all_logpath + ts + '.log'
#     error_logname = error_logpath + ts + '.log'
#
#     wall = logging.FileHandler(all_logname)
#     wall.setLevel(logging.DEBUG)
#     wr = logging.FileHandler(error_logname)
#     wr.setLevel(logging.DEBUG)
#     wk = logging.StreamHandler()
#     wk.setLevel(logging.DEBUG)
#
#     all_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#     error_log_formatter = logging.Formatter(
#         '%(asctime)s - %(name)s - %(levelname)s - %(module)s -%(lineno)s - %(message)s')
#     wall.setFormatter(all_log_formatter)
#     wr.setFormatter(error_log_formatter)
#     wk.setFormatter(all_log_formatter)
#     logger.addHandler(wall)
#     logger.addHandler(wr)
#     logger.addHandler(wk)
#     return logger



# class Log:
#     def __init__(self):
#         self.log_path = 'D:\PycharmProjects\\untitled\emp73\\report\log'
#         self.logname = os.path.join(self.log_path, '%s.log' % time.strftime('%Y_%m_%d'))
#         self.logger = logging.getLogger()
#         self.logger.setLevel(logging.DEBUG)
#         self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s[line:%(lineno)d] - fuc:%(funcName)s- %(levelname)s: %(message)s')
#     def __console(self, level, message):
#         # 创建一个FileHandler，用于写到本地
#         fh = logging.FileHandler(self.logname, 'a')  # 追加模式
#         fh.setLevel(logging.DEBUG)
#         fh.setFormatter(self.formatter)
#         self.logger.addHandler(fh)
#
#         # 创建一个StreamHandler,用于输出到控制台
#         ch = logging.StreamHandler()
#         ch.setLevel(logging.DEBUG)
#         ch.setFormatter(self.formatter)
#         self.logger.addHandler(ch)
#
#         if level == 'info':
#             self.logger.info(message)
#         elif level == 'debug':
#             self.logger.debug(message)
#         elif level == 'warning':
#             self.logger.warning(message)
#         elif level == 'error':
#             self.logger.error(message)
#         # 这两行代码是为了避免日志输出重复问题
#         self.logger.removeHandler(ch)
#         self.logger.removeHandler(fh)
#         # 关闭打开的文件
#         fh.close()
#
#     def debug(self, message):
#         self.__console('debug', message)
#
#     def info(self, message):
#         self.__console('info', message)
#
#     def warning(self, message):
#         self.__console('warning', message)
#
#     def error(self, message):
#         self.__console('error', message)