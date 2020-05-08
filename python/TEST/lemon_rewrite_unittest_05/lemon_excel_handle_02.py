#!/usr/bin/python
# -*-coding:UTF-8 -*-

# ========================
# @Time  : 2020/5/5
# @Author: Sunny
# ========================

#将excel重新封装以后，重写


#使用ddt来重构测试类
from ddt import ddt,data


import unittest
import inspect
#导入自定义模块
from TEST.lemon_unittest.lemon_unnitest_02 import MathOper
from TEST.lemon_rewrite_unittest_05.lemon_excel_handle_01 import HandleExecl
from collections import namedtuple

from openpyxl import load_workbook #可以对已存在的excel进行读写操作





@ddt
class TestMulti(unittest.TestCase):  #继承unittest.TeatCase类
    """
    测试两数相乘
    """
    case_obj = HandleExecl("test.xlsx")
    cases = case_obj.get_cases()  # 获取所有的用例，返回一个嵌套命名元组的列表


    @classmethod
    def setUpClass(cls):
        """
        打开文件
        :return:
        """
        # global file_name
        # global file
        print('\n{:=^40s}\n'.format('开始执行测试用例'))
        cls.file_name = 'homework.txt'
        print('打开【{}】文件'.format(cls.file_name))
        cls.file = open(cls.file_name, mode='a', encoding='utf-8')
        cls.file.write('\n{:=^40s}\n'.format('开始执行测试用例'))

    @classmethod
    def tearDownClass(cls):
        """
        重写父类的方法
        每一个用例执行以后会被调用
        :return:
        """
        print("\n{:=^40s}\n".format('用例执行结束'))
        print('关闭【{}】文件'.format(cls.file_name))
        cls.file.write('{:=^40s}\n'.format('用例执行结束'))
        cls.file.close()


    @data(*cases)
    def test_negatives_multi(self,data_namedtuple):  #测试用例方法名必须以test开头
        """
        测试2个负数相乘
        :return:
        """
        #能够查看当前运行的实例方法名称
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        case_id = data_namedtuple.case_id
        msg = data_namedtuple.title
        data_1 = data_namedtuple.data_1
        data_2 = data_namedtuple.data_2
        expext_xase = data_namedtuple.expext_xase

        #获取实际结果
        real_result = MathOper(data_1,data_2).multiply()
        #验证实际结果与预期结果是否一致
        expect_result = expext_xase
        #将实际结果写入excel

        try:
            self.assertEqual(expect_result,real_result,msg='测试{}失败'.format(msg))

        except AssertionError as e:
            print('具体异常为：{}'.format(e))
            self.file.write('{},执行结果为：{}\n具体异常为：{}\n'.format(msg, 'fail', e))
            self.cases_obj.write_result(row=case_id+1,actual=real_result,result="Fail") #将执行失败的用例fail

            raise e
        else:
            self.file.write('{},执行结果为：{}\n'.format(msg, 'pass'))
            self.case_obj.write_result(row=case_id+1,actual=real_result,result="pass") #将执行成功的用例写入pass


if __name__ == '__main__':
    unittest.main()