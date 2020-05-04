# -*- coding: utf-8 -*-


#先导入模块

import unittest
import inspect
from TEST.lemon_unittest.lemon_unnitest_02 import MathOper
#每一条用例使用一个实例方法来测试，并且实例方法名要以下划线test开头
class TestMulti(unittest.TestCase):  #定义一个测试类，继承unittest.TeatCase类
    def test_negatives_multi(self):  #测试用例方法名必须以test开头
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        #获取实际结果
        real_result = MathOper(-2,-4).multiply()
        #验证实际结果与预期结果是否一致
        expect_result = 8
        self.assertEqual(expect_result,real_result,msg='测试2个负数相乘失败')

    def test_neg_pos_multi(self):
        """
        2.测试一个正数一个负数相乘
        :return:
        """
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        real_result = MathOper(2, -5).multiply()
        expect_result = 10
        self.assertEqual(expect_result, real_result, msg='测试一个正数和一个负数相乘失败')

    def test_two_zero(self):
        """
        两个0相乘
        :return:
        """
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        real_result = MathOper(0, 0).multiply()
        expect_result = 0
        self.assertEqual(expect_result, real_result, msg='测试2个0相乘失败')

    def test_two_pos_muti(self):
        """
        两个正数相乘
        :return:
        """
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        real_result = MathOper(3, 5).multiply()
        expect_result = 13
        self.assertEqual(expect_result, real_result, msg='测试2个正数相乘失败')

if __name__ == '__main__':
    unittest.main()   #可以执行所有用例
    #在一个测试类中，用例执行的顺序是，实例方法名的ASCLL码数值从小到大的顺序


