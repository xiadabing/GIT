#!/usr/bin/python
# -*-coding:UTF-8 -*-

# ========================
# @Time  : 2020/5/7
# @Author: Sunny
# ========================

def print_params_3(*args,**kwargs):
    print(f'params为{args}')
    print(f'kw_params为{kwargs}')

user = ('可优','柠檬小姐姐',[1314,520])
love_time = {'time': 10000,"gift":"钻戒"}
print_params_3(*user,**love_time)

