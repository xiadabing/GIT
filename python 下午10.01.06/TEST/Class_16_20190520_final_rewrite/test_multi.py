#!/usr/bin/python
# -*-coding:UTF-8 -*-

# ========================
# @Time  : 2020/5/9
# @Author: Sunny
# ========================

#使用ddt来重构测试类
from ddt import ddt,data


import unittest
import inspect
from openpyxl import load_workbook #可以对已存在的excel进行读写操作
#导入自定义模块
from TEST.lemon_unittest.lemon_unnitest_02 import MathOper
from TEST.Class_16_20190520_final_rewrite.handle_excel import do_excel
from TEST.Class_16_20190520_final_rewrite.handle_config import do_config
from TEST.Class_16_20190520_final_rewrite.handle_log import do_log







@ddt
class TestMulti(unittest.TestCase):  #继承unittest.TeatCase类
    """
    测试两数相乘
    """
    #config = HandleConfing()
    #case_obj = HandleExecl(config("file path","cases_path")) #指定文件名
    #cases = case_obj.get_cases()  # 获取所有的用例，返回一个嵌套命名元组的列表
    cases = do_excel.get_cases()

    @classmethod
    def setUpClass(cls):
        """
        打开文件
        :return:
        """

        do_log.info('\n{:=^40s}\n'.format('开始执行测试用例'))

    @classmethod
    def tearDownClass(cls):
        """
        重写父类的方法
        每一个用例执行以后会被调用
        :return:
        """
        do_log.info('\n{:=^40s}\n'.format('用例执行结束'))


    @data(*cases)
    def test_negatives_multi(self,data_namedtuple):  #测试用例方法名必须以test开头
        """
        测试2个负数相乘
        :return:
        """
        do_log.info('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
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
        run_success_msg = do_config("msg","sussess_result")
        run_fail_msg = do_config("msg", "fail_result")
        try:
            self.assertEqual(expect_result,real_result,msg='测试{}失败'.format(msg))

        except AssertionError as e:
            do_log.error('具体异常为：{}'.format(e))
            do_excel.write_result(row=case_id+1,actual=real_result,result=run_fail_msg) #将执行失败的用例fail
            raise e
        else:
            do_excel.write_result(row=case_id+1,actual=real_result,result=run_success_msg) #将执行成功的用例写入pass


if __name__ == '__main__':
    unittest.main()