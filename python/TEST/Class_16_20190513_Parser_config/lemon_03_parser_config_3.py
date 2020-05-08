#!/usr/bin/python
# -*-coding:UTF-8 -*-

# ========================
# @Time  : 2020/5/7
# @Author: Sunny
# ========================


from configparser import ConfigParser
#1、创建配置文件解析器
config = ConfigParser() #没有读取配置文件时，config相当于一个空字典

#2、将需要写入配置文件中的数据组合为字典
datas = {
    "file path" : {
        "cases_path" : "test.xlsx",
        "log_path" : "homework.txt"
    },
    "msg" : {
        "sussess_result" : "Pass",
        "fail_result" : "Fail"
    },
    "excel" : {
        "actual_col" : 6,
        "result_col" : 7,
        "one_res" : 0,
        "two_res" : "yes"
    }
}


for key in datas:
    config[key] = datas[key]


#3、保存到文件
with open("write_config.ini","w") as file:
    config.write(file)

pass