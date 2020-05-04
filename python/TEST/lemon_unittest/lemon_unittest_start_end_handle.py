#处理测试用例执行之前和执行之后的操作

# -*- coding: utf-8 -*-



import unittest
import inspect
#导入自定义模块
from TEST.lemon_unittest.lemon_unnitest_02 import MathOper
class TestMulti(unittest.TestCase):  #继承unittest.TeatCase类
    """
    测试2数相乘
    """
    def setUp(self) -> None:
        """
        重写父类的方法
        在每一个用例执行之前会被调用
        :return:
        """
        print("{}".format('开始执行用例'))

    def test_negatives_multi(self):  #测试用例方法名必须以test开头
        """
        测试2个负数相乘
        :return:
        """
        #能够查看当前运行的实例方法名称
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        #获取实际结果
        real_result = MathOper(-2,-4).multiply()
        #验证实际结果与预期结果是否一致
        expect_result = -8
        try:
            self.assertEqual(expect_result,real_result,msg='测试2个负数相乘失败')

        except AssertionError as e:
            print('这里需要使用日志器来记录日志')
            print('具体异常为：{}'.format(e))
            raise e


    def test_neg_pos_multi(self):
        """
        2.测试一个正数一个负数相乘
        :return:
        """
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        real_result = MathOper(2, -5).multiply()
        expect_result = -10
        try:
            self.assertEqual(expect_result, real_result, msg='测试一个正数和一个负数相乘失败')
        except AssertionError as e:
            print('这里需要使用日志器来记录日志')
            print('具体异常为：{}'.format(e))
            #raise关键字是将某个异常主动抛出
            raise e


    def test_two_zero(self):
        """
        两个0相乘
        :return:
        """
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        real_result = MathOper(0, 0).multiply()
        expect_result = 0
        try:
            self.assertEqual(expect_result, real_result, msg='测试2个0相乘失败')
        except AssertionError as e:
            print('这里需要使用日志器来记录日志')
            print('具体异常为：{}'.format(e))
            raise e

    def test_two_pos_muti(self):
        """
        两个正数相乘
        :return:
        """
        print('\nRunning Test Method:{}'.format(inspect.stack()[0][3]))
        real_result = MathOper(3, 5).multiply()
        expect_result = 13
        try:
            self.assertEqual(expect_result, real_result, msg='测试2个正数相乘失败')
        except AssertionError as e:
            print('这里需要使用日志器来记录日志')
            print('具体异常为：{}'.format(e))
            raise e

    def tearDown(self) -> None:
        """
        重写父类的方法
        每一个用例执行以后会被调用
        :return:
        """
        print("{}".format('用例执行结束'))
if __name__ == '__main__':
    unittest.main()   #可以执行所有用例
    #在一个测试类中，用例执行的顺序是，实例方法名的ASCLL码数值从小到大的顺序
