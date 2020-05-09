#!/usr/bin/python
# -*-coding:UTF-8 -*-

# ========================
# @Time  : 2020/5/7
# @Author: Sunny
# ========================

#1、明确需求
#通过区域名以及选项名来获取选项值
#如果只传区域名，能够获取此区域下的所有选项，返回一个字典
#如果获取到的数据为数字类型的字符串，自动转化为python中的数字类型

#2、把固定的参数设置为属性值

#3、综合需求

#一个对象() #返回DEFAULT默认区域下的所有选项，构造成的 一个字典
#一个对象(区域名)        #能够获取此区域下所有选项，构造的一个字典
#一个对象(区域名，选项名)  #通过区域名以及选项名来获取选项值
#一个对象(is_eval=True) 将获取到的数据使用eval函数进行转换
#一个对象(is_bool=Ture) 将获取到的数据使用getbool()方法来获取

from configparser import ConfigParser


class HandleConfing(ConfigParser):  #继承configparser类
    """
    定义处理配置文件的类
    """
    def __init__(self):  #重写或者拓展父类的构造方法，往往需要先调用父类的构造方法
        #调用父类的构造方法
        super().__init__()
        self.filename = "testcase.conf"
        # HandleConfing继承了ConfigParser类，也可以说变成了ConfigParser的对象，
        # 因此可以用ConfigParser的read方法读取配置文件,也即是self.read()
        self.read(self.filename,encoding='utf-8')

    def __call__(self, section="DEFAULT",option=None,is_eval=False,is_bool=False):
        """
        '对象()' 这种形式，会直接调用__call__
        :param section: 区域名
        :param option:  选项名
        :param is_eval: 为默认参数，是否进行eval函数转换，默认不转换
        :param is_bool: 选项所对应的值，是否需要转换为bool类型，默认不转换
        :return:
        """
        if option is None:
            #一个对象(区域名),能够获取这个区域名下所有选项的值，构造成的一个字典
            return dict(self[section])

        if isinstance(is_bool,bool): #判断所传的值是否是布尔类型
            if is_bool:
                #一个对象(区域名,选项名，is_bool=True),将获取到的数据使用getboolean来转换为bool类型
                return self.getboolean(section,option)
        else:
            raise ValueError("is_bool 必须是布尔类型") #手动抛异常

        data = self.get(section,option)
        #如果获取到的数据为数字类型的字符串，自动转化成python中数字类型

        if data.isdigit(): #判断是否为数字类型的额字符串
            return int(data)
        try:
            return float(data) #如果为浮点类型的字符串，则直接转换
        except ValueError:
            pass

        if isinstance(is_eval,bool):
            if is_eval:
                # 一个对象(区域名,选项名，is_bool=True),将获取到的数据使用getboolean来转换为bool类型
                return eval(data)
        else:
            raise ValueError("is_eval 必须是布尔类型")  # 手动抛异常
        return data





if __name__ == '__main__':
    config = HandleConfing()
    # print(config())
    # print(config("excel"))
    # print(config("excel","two_res"))
    # print(config("excel", "two_res",is_bool=True))
    # print(config("excel", "five_res", is_eval=True))
    pass






# obj = Foo() #类名+括号  会自动调用__init__构造方法
# obj(10,20) #一个对象使用括号，(类似于函数的调用),那么会自动调用__call__

