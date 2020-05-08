#!/usr/bin/python
# -*-coding:UTF-8 -*-

# ========================
# @Time  : 2020/5/5
# @Author: Sunny
# ========================

#为了解决很多变量写死了，比如excel文件名、记录日志的文件名，若更改，比较麻烦，所以采用配置文件

#一般配置文件的拓展名为: .ini、conf等
#配置文件一般是什么样的呢？
"""
1.section 区域或者片段名[区域名]
2.区域名不必遵守python中的标识符命名规则
等号左边为选项名，右边为value
3.option 相当于字典里面的key
4.选项名是不区分大小写，默认以小写存储，选项名也不必遵守python命名
5.value 相当于字典中的value
6.给选项赋值，默认使用等号，也可以使用英文名

"""

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
# msg = config["msg"]  #返回一个section对象给msg,可以将msg类比于一个字典，可以转换一下msg=dict(config["msg"])
# for opt in msg:   #for循环以后，返回的是字典的key
#     print(opt)
#方法四
msg = dict(config['msg'])
#print(msg)
for key,value in msg.items():
    print(key,value)

#config类似于嵌套字典的字典，我们可以以字典的方式去使用
# config = {
#     "file path": {"cases_path":"test.xlsx","log_path":"homework.txt"},
#     "msg":{"sussess_result":"Pass","fail_result":"Fail"},
#     "excel":{"actual_col":6,"result_col":7}
# }

pass

