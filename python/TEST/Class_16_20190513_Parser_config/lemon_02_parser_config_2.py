#!/usr/bin/python
# -*-coding:UTF-8 -*-

# ========================
# @Time  : 2020/5/7
# @Author: Sunny
# ========================


from configparser import ConfigParser
#1、创建配置文件解析器
config = ConfigParser()

#2、指定读取的配置文件名
read_file = config.read("testcase.conf",encoding='utf-8')  #读取成功的文件，以字典类型返回


#3.读取数据
#config.sections()  #返回区域名（字符串）组成的列表

#获取选项值
#方法一
#print(config["file path"]["cases_path"])
#方法二
#config.get("file path","cases_path")

#方法三
# msg = dict(co
# 为:{}\n类型为:{}".format(value,type(value)))


#数据类型的转换
#从配置文件中获取的所有值都是字符串类型
#可以使用int来转换整数，也可以使用eval函数
#配置文件类中，提供了一个getint()
actual_col = config.getint("excel","actual_col")
print("值为:{}\n类型为:{}".format(actual_col,type(actual_col)))
print(config.getboolean("excel","one_res"))
#1、yes、on、true 都会被识别为Ture
#0、no、off、flase 都会被识别为Flase
#gitfloat() 将数字类型的字符串转换成float类型
#如果是其它类型、如列表、元组、字典、只能够使用eval函数

#配置文件中有一个默认的区域([DEFAULT]),这个区域中保存的是所有区域中公共的数据
#如果不显示定义[DEFAULT]，就是一个空字典
pass
