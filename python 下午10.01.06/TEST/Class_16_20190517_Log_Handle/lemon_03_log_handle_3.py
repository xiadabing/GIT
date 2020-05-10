#!/usr/bin/python
# -*-coding:UTF-8 -*-

# ========================
# @Time  : 2020-05-10
# @Author: Sunny
# ========================

#痛点：
# 所有的日志都保存在一个文件中，内存大，性能差
#日志文件无限大，会导致内存不够
#历史悠久的日志无价值可以删掉

#解决方案：
#使用轮询日志，限制单个文件的大小，需要使用RotatingFileHandler


import logging  #python系统自带的
from logging.handlers import RotatingFileHandler

#1、定义日志收集器
#返回Logger对象
case_logger = logging.getLogger("case") #如果不传name参数，那么默认使用root根收集器

#2、指定日志收集器的日志等级
case_logger.setLevel(logging.DEBUG)

#3、定义日志输出渠道(可以指定多个渠道)
#输出到console控制台
console_handle = logging.StreamHandler()
#输出到文件中
#file_handle = logging.FileHandler("case.log",encoding="utf-8")
#8bit = 1Bytes, 1024Bytes = 1KB, 1024KB = 1M, 1024M = 1GB
#backupCount 备份日志文件的数量
#maxBytes 一个日志文件最大的字节数
file_handle = RotatingFileHandler("case.log",maxBytes=1024 * 1024 *100,backupCount=3,encoding="utf-8")
#4、指定日志输出渠道的日志等级
#console_handle.setLevel(logging.ERROR)
console_handle.setLevel("ERROR")  #如果不能够被日志收集器收集的日志，一定没办法输出到渠道中
file_handle.setLevel(logging.INFO)

#5、定义日志显示的格式
#%(asctime)s  定义日志显示当前时间，系统固定写法
#%(levelname)s  日志等级名称
#%(message)s    日志信息
simple_formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - [日志信息]:%(message)s") #简单的日志格式
verbose_formatter = logging.Formatter("%(asctime)s - [%(levelname)s] - %(module)s -%(name)s -%(lineno)d- [日志信息]:%(message)s") #复杂的日志格式

console_handle.setFormatter(simple_formatter) #设置终端的日志为简单格式
file_handle.setFormatter(verbose_formatter)   #设置终端的日志为复杂格式

#6、对接，将日志收集器与输出渠道进行对接
case_logger.addHandler(console_handle)
case_logger.addHandler(file_handle)


if __name__ == '__main__':
    for _ in range(1000):
        case_logger.debug("这是debug日志")
        case_logger.info("这是nfo日志")
        case_logger.warning("这是warning日志")
        case_logger.error("这是error日志")
        case_logger.critical("这是critical日志")

